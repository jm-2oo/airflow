USE airflow_db;
DROP TABLE IF EXISTS main_tbl;
CREATE TABLE main_tbl (
    FruitID int,
    Fruit varchar(255),
    FruitColour varchar(255),
    Origin varchar(255)
    );