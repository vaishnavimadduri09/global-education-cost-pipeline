-- University Rankings dbt Model
-- This transforms our raw university data

WITH raw_data AS (
    SELECT
        world_rank,
        institution,
        country,
        score,
        year,
        broad_impact
    FROM {{ source('education_costs', 'university_rankings') }}
),

transformed AS (
    SELECT
        world_rank,
        institution,
        country,
        score,
        year,
        broad_impact,
        CASE
            WHEN world_rank <= 100 THEN 'Top 100'
            WHEN world_rank <= 500 THEN 'Top 500'
            WHEN world_rank <= 1000 THEN 'Top 1000'
            ELSE 'Rest'
        END AS rank_category,
        CASE
            WHEN score >= 90 THEN 'Excellent'
            WHEN score >= 80 THEN 'Good'
            ELSE 'Average'
        END AS score_category
    FROM raw_data
)

SELECT * FROM transformed