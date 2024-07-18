-- 코드를 작성해주세요
SELECT 
    c.ID AS ID,
    c.GENOTYPE AS GENOTYPE,
    p.GENOTYPE AS PARENT_GENOTYPE
FROM
    ECOLI_DATA AS c
JOIN
    ECOLI_DATA AS p
ON
    c.PARENT_ID=p.ID
WHERE
    p.GENOTYPE & c.GENOTYPE = p.GENOTYPE
ORDER BY c.ID