-- Write your query below
 SELECT c.name
 FROM customers c
 FULL JOIN orders o ON c.id = o.customer_id
 WHERE o.customer_id IS Null