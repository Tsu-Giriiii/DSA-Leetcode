# Write your MySQL query statement below
SELECT 
    d.name AS Department,
    e1.name AS Employee,
    e1.salary
FROM Employee e1
JOIN Department d ON e1.departmentId = d.id
WHERE 3 > (
    -- Subquery: Counts how many DISTINCT higher salaries exist in the same department
    SELECT COUNT(DISTINCT e2.salary)
    FROM Employee e2
    WHERE e2.departmentId = e1.departmentId
      AND e2.salary > e1.salary
)
ORDER BY d.name, e1.salary DESC;
    