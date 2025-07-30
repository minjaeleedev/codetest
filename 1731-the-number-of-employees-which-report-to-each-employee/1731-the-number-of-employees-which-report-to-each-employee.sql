# Write your MySQL query statement below
SELECT 
    r.employee_id as employee_id,
    r.name as name,
    COUNT(s.reports_to) as reports_count,
    ROUND(AVG(s.age)) as average_age
FROM Employees s
JOIN Employees r
ON s.reports_to = r.employee_id 
GROUP BY s.reports_to;