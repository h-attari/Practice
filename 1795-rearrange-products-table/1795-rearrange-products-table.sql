# Write your MySQL query statement below
Select product_id, "store1" as store, store1 as price
From Products
Where store1 is not null

Union

Select product_id, "store2" as store, store2 as price
From Products
Where store2 is not null

Union

Select product_id, "store3" as store, store3 as price
From Products
Where store3 is not null;