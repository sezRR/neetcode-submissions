SELECT name FROM sales_person sp
WHERE NOT EXISTS (
    SELECT 1 FROM orders o
    WHERE o.sales_id = sp.sales_id AND o.com_id = 1
);