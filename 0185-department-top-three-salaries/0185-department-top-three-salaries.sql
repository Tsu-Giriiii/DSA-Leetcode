# Write your MySQL query statement below
select Department,Employee,Salary
from (SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary as Salary,
    dense_rank() over(partition by d.id order by e.salary desc) as rnks
    from Employee e
    left join Department d on e.departmentId = d.id) as Ranked
where rnks <=3