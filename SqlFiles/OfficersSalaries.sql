SELECT
    title,
    AVG(total) AS avgSalaries
FROM
    officers
WHERE
    title IS NOT NULL
GROUP BY
    title
HAVING 
	AVG(total) IS NOT NULL
ORDER BY
    avgSalaries DESC;