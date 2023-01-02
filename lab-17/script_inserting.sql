/*  MySQL  */

insert into Post (title, text, date)
values 
    ('My first post', 'Hello, my dear subscribers. Welcome to my blog. And bla-bla-bla..', '2023-01-01'),
    ('My second post', 'text-text-text', '2023-01-01'),
    ('My third post about news', 'news-news-news', curdate());

insert into User (nickname, email)
values 
    ('Randy', 'random@gmail.com'),
    ('Weirny', 'weird@gmail.com');

insert into Comment (post_id, user_id, comment, date)
values
    (1, 1, 'cool!', curdate()),
    (1, 2, 'Gratz :0', curdate()),
    (2, 1, 'uhoo!', curdate());

insert into Tag (tag_name)
values ('daily'), ('news');

insert into Post_has_tag (post_id, tag_id)
values (1, 1), (2, 1), (3, 2);
