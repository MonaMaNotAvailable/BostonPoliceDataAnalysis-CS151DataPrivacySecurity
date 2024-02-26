SELECT 
    allegation,
    COUNT(*) AS frequency,
    ROUND((COUNT(*) * 100.0) / total.total_count, 2) AS percentage
FROM 
    bpd_allegations,
    (SELECT COUNT(*) AS total_count FROM bpd_allegations) AS total
GROUP BY 
    allegation, total.total_count
ORDER BY 
    frequency DESC;
