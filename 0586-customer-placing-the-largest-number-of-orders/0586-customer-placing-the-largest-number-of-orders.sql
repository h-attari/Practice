# Write your MySQL query statement below
Select customer_number
From Orders
Group By customer_number
Order By Count(customer_number) DESC
Limit 1;