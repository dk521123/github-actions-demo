WITH const AS (
    SELECT 365 * 2 AS interval_date
)

SELECT
    *
FROM
    project-name.`data-set-name`.schema-name,
    const
