-- Write your query below
SELECT sp.name
FROM sales_person sp
LEFT JOIN orders o ON sp.sales_id = o.sales_id
LEFT JOIN company c on c.com_id = o.com_id
GROUP BY sp.sales_id, sp.name
HAVING COUNT (*) FILTER (WHERE c.name = 'CRIMSON') = 0 ;