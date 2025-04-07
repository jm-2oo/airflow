SELECT 
street_crime_case_id
,b.location_name
,c.street_crime_category
,d.street_crime_outcome
FROM f_police_street_crime AS a 
LEFT JOIN d_street_crime_location AS b
ON a.FK_location_nameID = b.d_street_crime_location_ID 
LEFT JOIN d_street_crime_category AS c
ON a.FK_street_crime_categoryID = c.d_street_crime_category_ID
LEFT JOIN d_street_crime_outcome AS d
ON a.FK_street_crime_outcome_statusID = d.d_street_crime_outcome_ID 
WHERE 
	FK_street_crime_outcome_statusID <> -1 
ORDER BY RAND()
LIMIT 10;