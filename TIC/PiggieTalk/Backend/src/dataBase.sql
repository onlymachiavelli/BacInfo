create table users(
    id int(10) primary key auto_increment,
    name varchar(20) not null,
    email varchar(30) not null,
    password varchar(30)  not null,
    created_at date not null,
    friendN int(100) not null default 0,

);

)engine = innodb;

create table friends (
    id int(10) primary key autoincrement,
    user_id int(10) not null,
    friend_id integer not null,
    created_at date not null
);
)engine=innodb;