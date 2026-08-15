/* Write your T-SQL query statement below */
SELECT product_id
FROM Products as p
WHERE p.low_fats = 'Y' and p.recyclable = 'Y';