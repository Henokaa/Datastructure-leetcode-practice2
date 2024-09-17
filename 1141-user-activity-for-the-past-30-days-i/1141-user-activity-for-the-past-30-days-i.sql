# Write your MySQL query statement below,
# Because there could be 31 days, better to use DATEDIFF, 
/* active users 30 days, before 2019-07-27 */

select activity_date as day, count(DISTINCT user_id) as active_users
from Activity
where activity_date >= '2019-06-28' and activity_date <= '2019-07-27'
Group by activity_date

