/*  MySQL  */

-- The task is to use:
-- transactions (at least 2)
-- coalesce
-- cast
-- case when
-- use different datetime functions

start transaction;

insert into Post (title, text, date)
value ('Let`s write transaction', 'start transaction -> commit', curdate());

insert into Tag (tag_name)
value ('SQL');

insert into Post_has_tag (post_id, tag_id)
value (4, 3);

commit;


start transaction;

set @commit_date := date_add(cast("2023-01-03" as DATE), interval 1 day);

insert into User (nickname, email)
value ('SQLover', 'sqlfor@gmail.com');

insert into Comment (post_id, user_id, comment, date)
value (4, 3, 'awesome!', @commit_date);

commit;


select pt.post_id, pt.title, count(cm.comment) 'comment counter',
	case
		when count(cm.comment) < 1 then 'unpopular'
        when count(cm.comment) = 1 then 'popular'
        when count(cm.comment) > 1 then 'very popular'
    end as popularity
from post pt
left join comment cm on pt.post_id = cm.post_id
group by pt.post_id, pt.title
order by count(cm.comment) desc
