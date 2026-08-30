# Write your MySQL query statement below
select name as Employee from Employee as emp where salary > (select salary from Employee as mgr where mgr.id = emp.managerId)