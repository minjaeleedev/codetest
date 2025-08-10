# Write your MySQL query statement below
SELECT 
    h.name as Department,
    e.name as Employee,
    e.salary as Salary
FROM Employee e
JOIN (
    SELECT
        d.id as id,
        d.name as name,
        max(salary) as highest
    FROM Employee e
    JOIN Department d
    ON e.departmentId=d.id
    GROUP BY d.id
) as h
ON e.departmentId=h.id
WHERE e.salary=h.highest;