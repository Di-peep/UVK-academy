/*  MySQL  */

-- The task is to write:
-- 	Noncorrelated and Correlated Subqueries in Select
-- 	Write at least one From clause with subquery in it
-- 	Write at least one Where clause with subquery in it
-- 	Use WITH clause (Common Table Expression)
-- 	Group the data by some field and filter it with Having clause
-- 	Use Order by
-- 	Use Limit

-- Find posts with max count comments
select pt.post_id, pt.title, count(cm.comment) 'comment counter'
from post pt
join comment cm on pt.post_id = cm.post_id
group by pt.post_id, pt.title
having count(cm.comment) = (
    select count(cm.comment)
    from comment cm
    group by cm.post_id
    order by 1 desc
    limit 1
);

-- From clause with subquery in it
select res.*, us.*
from (
    select pt.post_id, pt.title, pt.date 'post_date', cm.user_id, cm.date 'comment_date'
    from post pt
    join comment cm on pt.post_id = cm.post_id
    where pt.date = curdate()
) as res
join user us on res.user_id = us.user_id;

-- Where clause with subquery in it
select *
from post
where post.date in (
    select min(comment.date)
    from comment
);

-- Join User table and Comment table using WITH
with 
    cte1 as (select user_id, nickname from user),
    cte2 as (select user_id, comment from comment)
select * from cte1 join cte2 on ct1.user_id = cte2.user_id

