-- Write your query below
-- select s.name from 

-- sales_person s left join orders o on s.sales_id = o.sales_id 

-- left join company c on o.com_id = c.com_id 
-- where c.name != 'CRIMSON'

SELECT sp.name
FROM sales_person sp
WHERE sp.sales_id NOT IN (
    SELECT o.sales_id
    FROM orders o
    JOIN company c ON o.com_id = c.com_id
    WHERE c.name = 'CRIMSON'
);