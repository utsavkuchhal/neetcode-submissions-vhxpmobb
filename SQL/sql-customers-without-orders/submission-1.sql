-- Write your query below
SELECT name from CUSTOMERS c
    LEFT JOIN ORDERS o ON c.id = o.customer_id WHERE o.id IS NULL;
