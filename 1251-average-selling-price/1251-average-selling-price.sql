# Write your MySQL query statement below
SELECT
    p.product_id,
    IFNULL(ROUND(SUM(p.price * u.units) / SUM(u.units), 2), 0) AS average_price
FROM
    Prices p
LEFT JOIN
    UnitsSold u
ON
    p.product_id = u.product_id
AND
    U.PURCHASE_DATE >= P.START_DATE AND U.PURCHASE_DATE <= P.END_DATE
GROUP BY
    p.product_id;




