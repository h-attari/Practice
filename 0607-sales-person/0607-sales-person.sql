# Write your MySQL query statement below
Select name
From SalesPerson
Where name Not In
(
    Select s.name
    From SalesPerson s Left Join Orders o
    On s.sales_id = o.sales_id
    Left Join Company c
    On o.com_id = c.com_id
    Where c.name Like "RED"
);