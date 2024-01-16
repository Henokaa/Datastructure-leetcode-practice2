# Write your MySQL query statement below
Select
    employeeUNI.unique_id, employees.name
From 
    Employees
Left join EmployeeUNI ON employees.id = employeeUNI.id
