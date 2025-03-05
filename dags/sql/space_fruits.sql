USE fruit_bowl;

DROP TABLE IF EXISTS space_fruits;

CREATE TABLE space_fruits (
    people VARCHAR(255) NULL, 
    number VARCHAR(255) NULL,
    message VARCHAR(255) NULL 

);

LOAD DATA INFILE '/var/lib/mysql-files/api_py_table_load.csv'  
INTO TABLE space_fruits 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;