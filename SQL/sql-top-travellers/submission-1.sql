-- Write your query below
select name, coalesce(travelled_distance,0) as travelled_distance from (
select r.user_id, u.name, sum(r.distance) as travelled_distance from users u left join rides r on u.id = r.user_id 
group by r.user_id, u.name )
order by 2 desc, 1 asc