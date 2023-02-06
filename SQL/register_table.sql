create table register(
    user_id varchar(10),
    username varchar(100),
    password varchar(100),
    register_ts bigint,
    PRIMARY KEY (username)
);
