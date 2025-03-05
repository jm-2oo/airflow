USE airflow_db;
DROP TABLE IF EXISTS add_rows;
CREATE TABLE add_rows (
    FruitID int,
    Fruit varchar(255),
    FruitColour varchar(255),
    Origin varchar(255)
    );