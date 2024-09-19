# Write your MySQL query statement below
# largest single number, single, large

select max(unique_number.num) as num
from (
    select num
    from mynumbers
    Group by num
    having count(num) = 1
) as unique_number

