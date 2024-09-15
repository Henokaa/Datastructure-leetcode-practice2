# Write your MySQL query statement below
# count_id group, count, percent(x/ken(user_id))
select contest_id, ROUND (count(user_id) * 100 / (select Count(*) From Users), 2) AS percentage 
From Register
Group By contest_id
order by percentage DESC, contest_id;