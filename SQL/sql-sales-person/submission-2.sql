SELECT name FROM sales_person sp
WHERE sp.sales_id NOT IN (
    SELECT o.sales_id FROM orders o
    JOIN company c USING(com_id)
    WHERE o.sales_id = sp.sales_id AND c.name = 'CRIMSON'
);