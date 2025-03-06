USE police_db;

DROP TABLE IF EXISTS d_street_crime_outcome;

CREATE TABLE d_street_crime_outcome (
    d_street_crime_outcome_ID int NOT NULL AUTO_INCREMENT,
    street_crime_outcome VARCHAR(255) NOT NULL,
    CONSTRAINT PK_case_outcome PRIMARY KEY (street_crime_outcome, d_street_crime_outcome_ID),
    KEY (d_street_crime_outcome_ID) /*must create a key id*/
);

INSERT INTO d_street_crime_outcome (street_crime_outcome)
    SELECT 
        DISTINCT outcome_status_category AS street_crime_outcome
    FROM impt_police_street_crime
    WHERE outcome_status_category <> '';