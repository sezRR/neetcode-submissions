SELECT DISTINCT ON(student_id) student_id, exam_id, MAX(score) "score" FROM exam_results
GROUP BY student_id, exam_id
ORDER BY student_id, score DESC, exam_id ASC;