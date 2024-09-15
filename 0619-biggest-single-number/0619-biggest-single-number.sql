# Write your MySQL query statement below
# learn when to use have, when to use where
SELECT 
IFNULL((
    SELECT num 
    FROM MyNumbers
    GROUP BY num 
    HAVING COUNT(num) <= 1 
    ORDER BY num DESC LIMIT 1), NULL)
AS num;

