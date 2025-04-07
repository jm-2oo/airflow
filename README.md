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

### Streamlit app 
- (work in progress - looking to host MySQL db on public cloud infrastructure)
- https://jm-2oo-streamlit-police-page-nav-bgy9cx.streamlit.app
- Streamlit repo: https://github.com/jm-2oo/streamlit_police

### Architecture Diagram

![airflow architecture](https://github.com/jm-2oo/airflow/blob/main/images/police_architecture.png)

### Airflow Workflow
![airflow workflow](https://github.com/jm-2oo/airflow/blob/main/images/police.png)

## What I learnt
- From using Airflow I learnt a way of using Python in an ETL workflow
- How SQL queries can either be hardcoded or stored in a separate file and then executed with a Python script
- How to use Python connectors to connect to a MySQL database
- How transform and load API data from a JSON data type into a dataframe
