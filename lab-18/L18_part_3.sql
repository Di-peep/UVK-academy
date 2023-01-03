/*  MySQL  */

-- The task is to use:
-- INNER, LEFT, RIGHT, OUTER joins
-- USING
-- NATURAL JOIN
-- CROSS JOIN
-- SELF JOIN
-- UNION
-- EXCEPT and INTERSECT

select title, comment
from post
left join comment using (post_id);

select *
from comment
right join user using (user_id);

select title, group_concat(tag_name)
from tag
right join post_has_tag pht using (tag_id)
inner join post using (post_id)
group by post.title;

select title, date
from post
where date >= '2023-01-03'
union
select title, date
from post
where date <= '2023-01-02';

-- doesn't work in MySQL
select title, date
from post
where date >= '2023-01-03'
intersect -- or except
select title, date
from post
where date <= '2023-01-02';