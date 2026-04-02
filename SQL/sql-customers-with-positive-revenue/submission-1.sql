-- Write your query below
SELECT DISTINCT(customer_id)
FROM customers
WHERE customers.year = '2020'
GROUP BY customers.customer_id, customers.revenue
HAVING customers.revenue >0