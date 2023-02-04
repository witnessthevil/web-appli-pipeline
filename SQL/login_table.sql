create table mc_user_login(
    id bigint,
    user_id bigint,
    ip varchar(255),
    login_tm bigint(20),
    logout_tm bigint(20)
)