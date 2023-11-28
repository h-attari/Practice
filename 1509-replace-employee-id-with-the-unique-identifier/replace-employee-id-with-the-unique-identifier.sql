# Write your MySQL query statement below
SELECT emp_id.unique_id, emp.name
FROM Employees emp LEFT JOIN EmployeeUNI emp_id
ON emp.id = emp_id.id;