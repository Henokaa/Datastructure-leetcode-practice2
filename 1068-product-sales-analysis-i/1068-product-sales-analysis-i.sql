# Write your MySQL query statement below
Select product_name, year, price
From sales
Inner join product on product.product_id = sales.product_id;