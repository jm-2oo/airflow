## Intro
Hello, this is a personal data engineering project for me to experiment and learn from.

## Objectives
- Learn Python
- Learn how to install and use Airflow
- Learn how to use data from an API
- Create a simple ETL process using data engineering principles
- Test, break and experiment

## My Airflow Architecture
- To start off learning how to extract API data, I used a very simple dataset provided by data.police.uk containing logs of street crimes reported in the area

- I chose to use Airflow as an orchestrator for my ETL pipeline as it's open source with information freely available for me to learn from

- The purpose of the ETL process is to extract the API data and convert into fact / dim tables in a SQL database to be used further on in BI reporting

### Architecture Diagram

![airflow architecture]

### Airflow Workflow
![airflow workflow](https://github.com/jm-2oo/airflow/blob/main/images/police.png)
