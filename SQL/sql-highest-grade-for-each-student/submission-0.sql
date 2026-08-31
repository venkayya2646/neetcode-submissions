-- Write your query below

select student_id, exam_id, score from (
select student_id, exam_id, score, row_number() over(partition by student_id order by score desc, exam_id asc) as rnum from exam_results
) 
where rnum =1