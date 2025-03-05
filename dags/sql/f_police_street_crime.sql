USE police_db;

/*create empty calc fact table*/
DROP TABLE IF EXISTS calc_police_street_crime;

CREATE TABLE calc_police_street_crime (
    street_crime_case_id INT NOT NULL, 
    case_status_date VARCHAR(255) NULL,
    location_name_NatID VARCHAR(255) NULL,
    outcome_status_NatID VARCHAR(255) NULL,
    street_category_NatID VARCHAR(255) NULL
);

/*insert fact NatIDs*/
INSERT INTO calc_police_street_crime (street_crime_case_id, case_status_date, location_name_NatID, outcome_status_NatID, street_category_NatID)

SELECT 
    id AS street_crime_case_id,
    outcome_status_date AS case_status_date, 
    CONCAT(location_street_name, "||", location_street_id) AS location_name_NatID,
    outcome_status_category AS outcome_status_NatID,
    category AS street_category_NatID
FROM impt_police_street_crime;


/*create empty fact table*/
DROP TABLE IF EXISTS f_police_street_crime;

CREATE TABLE f_police_street_crime (
    street_crime_case_id INT,
    case_status_date VARCHAR(255),
    FK_location_nameID VARCHAR(255),
    FK_street_crime_outcome_statusID VARCHAR(255),
    FK_street_crime_categoryID VARCHAR(255)
     
);

/*insert data into fact table and join dimensions*/
INSERT INTO f_police_street_crime (street_crime_case_id, case_status_date, FK_location_nameID, FK_street_crime_outcome_statusID, FK_street_crime_categoryID)

SELECT 
    IFNULL(street_crime_case_id, 'Unknown') AS street_crime_case_id, 
    IFNULL(case_status_date, 'Unknown') AS case_status_date,
    IFNULL(d_street_crime_location.d_street_crime_location_ID, -1) AS FK_location_nameID,
    IFNULL(d_street_crime_outcome.d_street_crime_outcome_ID, -1) AS FK_street_crime_outcome_statusID,
    IFNULL(d_street_crime_category.d_street_crime_category_ID, -1) AS FK_street_crime_categoryID
FROM calc_police_street_crime AS calc 
    LEFT JOIN d_street_crime_location AS d_street_crime_location ON d_street_crime_location.location_name_NatID = calc.location_name_NatID
    LEFT JOIN d_street_crime_outcome AS d_street_crime_outcome ON d_street_crime_outcome.street_crime_outcome = calc.outcome_status_NatID
    LEFT JOIN d_street_crime_category AS d_street_crime_category on d_street_crime_category.street_crime_category = calc.street_category_NatID;
