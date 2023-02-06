create table mc_user_login(
    id bigint NOT NULL AUTO_INCREMENT,
    user_id varchar(10),
    ip varchar(20),
    login_tm bigint(20),
    logout_tm bigint(20),
    PRIMARY KEY (id)
);