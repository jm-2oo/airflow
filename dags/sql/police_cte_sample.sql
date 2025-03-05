WITH 
    cte1 AS (
        SELECT 
            location_street_name, 
            CONCAT(location_street_name, "||", location_street_id) AS NatID_street_name,
            location_street_id
        FROM impt_police_street_crime 
    ),
    cte2 AS (
        SELECT 
            street_name, 
            NatID_street_name 
        FROM d_street_name
    )

    /*join dimensions*/
    SELECT 
        /*cte1.location_street_id,*/
        IFNULL(cte2.street_name, -1) AS street_name 
        FROM cte1
    LEFT JOIN cte2 ON cte1.NatID_street_name = cte2.NatID_street_name; 