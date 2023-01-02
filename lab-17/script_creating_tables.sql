/*  MySQL  */

create schema if not exists `lab-17`;
use `lab-17`;

create table Post (
    post_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) UNIQUE,
    text TEXT NOT NULL,
    date DATE
);

create table User (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    nickname VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE
);

create table Comment (
    comment_id INT PRIMARY KEY AUTO_INCREMENT,
    post_id INT,
    user_id INT,
    comment TEXT NOT NULL,
    date DATE,
    FOREIGN KEY (post_id) REFERENCES Post(post_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

create table Tag (
    tag_id INT PRIMARY KEY AUTO_INCREMENT,
    tag_name VARCHAR(255) NOT NULL UNIQUE
);

create table Post_has_tag (
    post_id INT,
    tag_id INT,
    CONSTRAINT PK_Post_Tag PRIMARY KEY (post_id, tag_id),
    FOREIGN KEY (post_id) REFERENCES Post(post_id),
    FOREIGN KEY (tag_id) REFERENCES Tag(tag_id)
);

create table File (
    file_id INT PRIMARY KEY AUTO_INCREMENT,
    post_id INT,
    filename VARCHAR(255) NOT NULL UNIQUE,
    alttext VARCHAR(255) NOT NULL,
    file BLOB,
    FOREIGN KEY (post_id) REFERENCES Post(post_id)
);

create view comments_report as
select pt.title, pt.date 'post_date', cm.comment, us.nickname, cm.date 'comment_date'
from post pt
join comment cm on pt.post_id = cm.post_id
join user us on cm.user_id = us.user_id;
