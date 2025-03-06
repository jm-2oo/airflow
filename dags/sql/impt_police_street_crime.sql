USE police_db;

DROP TABLE IF EXISTS impt_police_street_crime;

CREATE TABLE impt_police_street_crime (
    category VARCHAR(255) NULL,
    location_type VARCHAR(255) NULL,
    context VARCHAR(255) NULL,
    outcome_status VARCHAR(255) NULL,
    persistent_id VARCHAR(255) NULL,
    id VARCHAR(255) NULL,
    location_subtype VARCHAR(255) NULL,
    month VARCHAR(255) NULL,
    location_latitude VARCHAR(255) NULL,
    location_street_id VARCHAR(255) NULL,
    location_street_name VARCHAR(255) NULL,
    location_longitude VARCHAR(255) NULL,
    outcome_status_category VARCHAR(255) NULL,
    outcome_status_date VARCHAR(255) NULL
);

LOAD DATA INFILE '/var/lib/mysql-files/police_street_crime.csv'  
INTO TABLE impt_police_street_crime 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;