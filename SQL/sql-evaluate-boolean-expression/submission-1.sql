-- Write your query below

-- select e.left_operand, e.operator, e.right_operand, case when 
-- operator = '>' then left_operand > right_operand 
-- when operator = '<' then left_operand < right_operand
-- when operator = '=' then left_operand = right_operand 
-- end as value

-- from variables v inner join expressions e on v.name = e.left_operand

SELECT
    e.left_operand,
    e.operator,
    e.right_operand,
    CASE
        WHEN e.operator = '>' AND lv.value > rv.value THEN 'true'
        WHEN e.operator = '<' AND lv.value < rv.value THEN 'true'
        WHEN e.operator = '=' AND lv.value = rv.value THEN 'true'
        ELSE 'false'
    END AS value
FROM expressions e
JOIN variables lv ON e.left_operand = lv.name
JOIN variables rv ON e.right_operand = rv.name;