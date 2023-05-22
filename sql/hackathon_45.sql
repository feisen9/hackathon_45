drop database if exists hackathon_45;
create database hackathon_45;

use hackathon_45;

drop table if exists `comment`;
drop table if exists `user`;
drop table if exists content;
drop table if exists tag;

#user table
create table user(
id int auto_increment,
username varchar(32) not null,
pass varchar(32) not null,
birthday datetime,
icon varchar(128),
email varchar(32),
phone varchar(11),
created_at timestamp not null,
updated_at timestamp not null,
primary key(id)
)charset = utf8mb4;

#content table
create table content(
id int auto_increment,
title varchar(32),
summary varchar(255),
contenttype varchar(16),
numlike int,
numview int,
created_at timestamp,
updated_at timestamp,
primary key(id)
)charset = utf8mb4;

create table photoset(
id int,
filepath varchar(128),
photorank int,
primary key(id)
)charset = utf8mb4;

create table book(
id int, 
bookname varchar(64),
author varchar(64),
bookinfo varchar(256),
bookcontent text,
photosetid int,
primary key(id),
foreign key(photosetid) references photoset(id),
foreign key(id) references content(id)
)charset = utf8mb4;

create table article(
id int,
articlename varchar(64),
author varchar(64),
articleinfo varchar(256),
articlecontent text,
photosetid int,
primary key(id),
foreign key(photosetid) references photoset(id),
foreign key(id) references content(id)
)charset = utf8mb4;

create table photo(
id int,
photoname varchar(64),
author varchar(64),
photoinfo varchar(256),
photosetid int,
primary key(id),
foreign key(photosetid) references photoset(id),
foreign key(id) references content(id)
)charset = utf8mb4;


create table `comment`(
userid int,
contentid int,
commentstr varchar(512),
updated_at timestamp,
primary key(userid, contentid),
foreign key(userid) references user(id),
foreign key(contentid) references content(id)
)charset = utf8mb4;

create table userlike(
userid int,
contentid int,
primary key(userid, contentid),
foreign key(userid) references user(id),
foreign key(contentid) references content(id)
)charset = utf8mb4;

create table tag(
tagname varchar(32) unique
)charset = utf8mb4;








