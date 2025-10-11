# Write your MySQL query statement below
SELECT machine_id,
    round(sum(case when activity_type='start' then timestamp*-1 else timestamp END)*1.0/(SELECT COUNT(DISTINCT process_id)),3) as processing_time
FROM Activity
GROUP BY machine_id