USE police_db;

DROP TABLE IF EXISTS d_street_crime_location;

CREATE TABLE d_street_crime_location (
    d_street_crime_location_ID int NOT NULL AUTO_INCREMENT,
    location_name VARCHAR(255) NOT NULL,
    location_name_id VARCHAR(255) NOT NULL, 
    location_name_NatID VARCHAR (255) NOT NULL,
    CONSTRAINT PK_street_name PRIMARY KEY (location_name, d_street_crime_location_ID),
    KEY (d_street_crime_location_ID) /*must create a key id*/
);

INSERT INTO d_street_crime_location (location_name, location_name_id, location_name_NatID)
    SELECT 
        DISTINCT location_street_name AS location_name,
        location_street_id AS location_id,
        CONCAT(location_street_name, "||", location_street_id) AS location_name_NatID
    FROM impt_police_street_crime
    WHERE location_street_name <> '';