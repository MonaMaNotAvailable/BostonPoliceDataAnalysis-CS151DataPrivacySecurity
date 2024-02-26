SELECT
    neighborhood,
    COUNT(*) AS frequency
FROM
    bpd_allegations
WHERE
    neighborhood IS NOT NULL
GROUP BY
    neighborhood
ORDER BY
    frequency DESC;
