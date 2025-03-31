# Write your MySQL query statement below
select p.product_name, sum(o.unit) as unit
from Products p JOIN Orders o using (product_id)
where o.order_date between "2020-02-01" and "2020-02-29"
group by product_id
having sum(o.unit) >= 100;