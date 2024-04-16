SELECT
    neighborhood,
    COUNT(*) AS totalVictims
FROM
    shootings
WHERE
    neighborhood IS NOT NULL
GROUP BY
    neighborhood
ORDER BY
    totalVictims DESC;

-- SELECT
--     *
-- FROM
--     shootings
-- WHERE
--     neighborhood = 'South Boston Waterfront' OR neighborhood = 'Beacon Hill';

-- SELECT
--     month,
--     COUNT(*) AS totalVictims
-- FROM
--     shootings
-- WHERE
--     month IS NOT NULL
-- GROUP BY
--     month
-- ORDER BY
--     totalVictims DESC;