from flask import Flask, render_template, request, session, flash, redirect, url_for
from flask_mysqldb import MySQL
from datetime import datetime, timezone
import time
import random
import string

app = Flask(__name__)
app.secret_key = "super secret key"
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'example'
app.config['MYSQL_DB'] = 'test'
mysql = MySQL(app)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login",methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('''select * from register where username =%s''',[username])
        data = cursor.fetchone()
        if data is not None:
            if password != data[2]:
                flash("your password is incorrect")
                render_template("login.html")
            else:
                session['user_id'] = data[0]
                session['username'] = data[1]
                session['login_ts'] = int(time.mktime(datetime.now().timetuple()))
                flash("you have successfully login")
                return redirect(url_for('home'))
        else:
            flash("Username does not exsits")
            render_template("login.html")

    return render_template("login.html")

@app.route("/signup",methods=['POST', 'GET'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html")
    if request.method == 'POST':
        user_id = ''.join(random.choice(string.digits + string.ascii_letters) for _ in range(10))
        username = request.form['username']
        password = request.form['password']
        ts = int(time.mktime(datetime.now().timetuple()))
        cursor = mysql.connection.cursor()
        cursor.execute('''select * from register where username =%s''',[username])
        data = cursor.fetchone()
        if data is None:
            cursor.execute(''' INSERT INTO register VALUES(%s,%s,%s,%s)''',(user_id,username,password,ts))
            mysql.connection.commit()
            cursor.close()
            flash("now login please")
            return redirect(url_for('login'))
        else:
            flash("this username have already been registered by others")
            render_template("signup.html")
    return render_template("signup.html")

@app.route("/logout")
def logout():
    user_id = session.get("user_id",None)
    if user_id is not None:
        logout_ts = int(time.mktime(datetime.now().timetuple()))
        cursor = mysql.connection.cursor()
        ip_list = ['101.33.32.0','101.33.32.1','101.33.32.2','101.33.32.3']
        cursor.execute(''' INSERT INTO mc_user_login(user_id,ip,login_tm,logout_tm)
         VALUES(%s,%s,%s,%s)''',(session['user_id'],random.choice(ip_list),session['login_ts'],logout_ts))
        mysql.connection.commit()
        cursor.close()
        session.clear()
        flash("you have successfully logout")
        return redirect(url_for("home"))
    else:
        flash("you have not login yet")
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)