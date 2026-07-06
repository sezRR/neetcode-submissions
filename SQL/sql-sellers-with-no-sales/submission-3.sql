SELECT s.seller_name
FROM seller s
WHERE NOT EXISTS (
    SELECT 1 FROM orders oo
    WHERE oo.seller_id = s.seller_id
      AND oo.sale_date >= DATE '2020-01-01'
      AND oo.sale_date <  DATE '2021-01-01'
)
ORDER BY s.seller_name;