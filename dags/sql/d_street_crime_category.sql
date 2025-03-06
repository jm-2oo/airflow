USE police_db;

DROP TABLE IF EXISTS d_street_crime_category;

CREATE TABLE d_street_crime_category (
    d_street_crime_category_ID INT NOT NULL AUTO_INCREMENT,
    street_crime_category VARCHAR(255) NOT NULL,
    CONSTRAINT PK_street_crime_category PRIMARY KEY (street_crime_category, d_street_crime_category_ID),
    KEY (d_street_crime_category_ID)
);

INSERT INTO d_street_crime_category (street_crime_category)
    SELECT 
        DISTINCT category AS street_crime_category
    FROM impt_police_street_crime
    WHERE category <> '';
