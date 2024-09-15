# Write your MySQL query statement below,
# Because there could be 31 days, better to use DATEDIFF, 
select activity_date as day, count(Distinct user_id) as active_users
from Activity
where activity_date BETWEEN "2019-06-28" AND "2019-07-27"
group by activity_date
