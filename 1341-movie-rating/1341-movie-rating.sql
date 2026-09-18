# Write your MySQL query statement below
(select u.name as results
from MovieRating m
left join Users u
on u.user_id = m.user_id
group by m.user_id
order by count(rating) desc, u.name asc
limit 1)

union all

(select m2.title as results
from MovieRating m
left join Movies m2
on m.movie_id = m2.movie_id
where date_format(m.created_at, '%Y-%m') = '2020-02'
group by m.movie_id
order by avg(m.rating) desc ,m2.title
limit 1)