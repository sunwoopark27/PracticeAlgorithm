WITH GRADE_AVERAGE AS(
      SELECT EMP_NO, 
             CASE
                WHEN AVG(SCORE) >= 96 THEN 'S'
                WHEN AVG(SCORE) >= 90 THEN 'A'
                WHEN AVG(SCORE) >= 80 THEN 'B'
                ELSE 'C'
             END AS 'GRADE'
      FROM HR_GRADE
      GROUP BY EMP_NO
)
SELECT 
    E.EMP_NO, E.EMP_NAME,
    A.GRADE,
    CASE
        WHEN A.GRADE = 'S' THEN E.SAL*0.2
        WHEN A.GRADE = 'A' THEN E.SAL*0.15
        WHEN A.GRADE = 'B' THEN E.SAL*0.1
        ELSE 0
    END AS 'BONUS'
FROM HR_EMPLOYEES E
LEFT JOIN GRADE_AVERAGE A
    ON E.EMP_NO = A.EMP_NO    
ORDER BY EMP_NO;