-- LIST NUMBER OF RECORDS WITH SAME SCORE
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY number DESC; 