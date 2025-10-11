# Write your MySQL query statement below
SELECT score, dense_rank() over(order by score desc) as `rank`
FROM Scores
ORDER BY score desc