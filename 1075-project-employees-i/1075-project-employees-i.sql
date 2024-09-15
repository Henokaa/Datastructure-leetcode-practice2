# Write your MySQL query statement below
# rounded 2 digits, inner join, average (experience)

select project_id, ROUND(avg(experience_years), 2) as average_years
from Project p
inner join Employee e on p.employee_id = e.employee_id
group by project_id
