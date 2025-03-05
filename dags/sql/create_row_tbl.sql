USE airflow_db;
DROP TABLE IF EXISTS row_tbl;
CREATE TABLE row_tbl (
    FruitID int,
    Fruit varchar(255),
    FruitColour varchar(255),
    Origin varchar(255)
    );