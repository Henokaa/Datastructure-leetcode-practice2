# Write your MySQL query statement below
# odd number and not "boring"
select id, movie, description, rating
from cinema
where id%2 != 0 and description != "boring"
order by rating DESC
