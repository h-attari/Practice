# Write your MySQL query statement below
Select event_day As day, emp_id,
Sum(out_time - in_time) As total_time
From Employees
Group By event_day, emp_id
Order By event_day ASC;