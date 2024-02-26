WITH TotalAllegations AS (
    SELECT COUNT(*) AS total FROM public.bpd_allegations
)
SELECT
    o.first_name,
    o.last_name,
    o.rank,
    COALESCE(o.neighborhood, oe.neighborhood)AS neighborhood,
    COUNT(a.allegation)/2 AS allegation_count,
    ROUND((COUNT(a.allegation) * 100.0) / ta.total, 2) AS allegation_percentage
FROM
    public.bpd_officers o
LEFT JOIN
    public.bpd_allegations a ON o.badge = a.badge
LEFT JOIN
    public.wwp_officers oe ON o.employee_id = oe.employee_id
CROSS JOIN
    TotalAllegations ta
WHERE
    o.active = TRUE
GROUP BY
    o.first_name,
    o.last_name,
    o.rank,
    COALESCE(o.neighborhood, oe.neighborhood),
    ta.total
ORDER BY
    allegation_count DESC;
