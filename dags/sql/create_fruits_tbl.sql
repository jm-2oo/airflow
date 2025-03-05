USE airflow_db;

DROP TABLE IF EXISTS fruits;

CREATE TABLE fruits (
    fruit VARCHAR(255) NULL, 
    colour VARCHAR(255) NULL,
    weight DECIMAL NULL
);

LOAD DATA INFILE '/var/lib/mysql-files/fruits.csv' 
INTO TABLE fruits 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;