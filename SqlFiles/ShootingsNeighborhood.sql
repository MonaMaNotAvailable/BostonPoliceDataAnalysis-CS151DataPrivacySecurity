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