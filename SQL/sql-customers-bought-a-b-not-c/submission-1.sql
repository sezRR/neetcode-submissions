SELECT c.customer_id, c.customer_name FROM customers c
JOIN orders o USING(customer_id)
WHERE o.product_name IN ('A', 'B') AND NOT EXISTS (
    SELECT 1 FROM orders oo
    WHERE oo.customer_id = c.customer_id AND oo.product_name = 'C'
)
GROUP BY c.customer_id
HAVING COUNT(DISTINCT(o.product_name)) = 2
ORDER BY c.customer_name;