# Write your MySQL query statement below
SELECT e.employee_id as employee_id
FROM Employees e
LEFT JOIN Employees m
ON e.manager_id = m.employee_id and e.manager_id is not null
WHERE e.manager_id is not null and m.employee_id is null and e.salary < 30000
