from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from datetime import datetime, timezone
import time
import random
import string

app = Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'example'
app.config['MYSQL_DB'] = 'test'
mysql = MySQL(app)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login")
def login():
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
        cursor.execute(''' INSERT INTO register VALUES(%s,%s,%s,%s)''',(user_id,username,password,ts))
        mysql.connection.commit()
        cursor.close()
        return render_template("login.html")
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)