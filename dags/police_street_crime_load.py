#get police street crime api data#
#convert JSON to dataframe#
#save to CSV#
#create SQL table#
#load CSV file to db#

from datetime import datetime, timedelta 
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow import DAG
from airflow.decorators import task 
from airflow.operators.python import PythonOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator

import requests
import json
import pandas as pd
import csv 

#get street level crime api data
def get_api():
    data = requests.get("https://data.police.uk/api/crimes-street/all-crime?date=2024-01&lat=52.629729&lng=-1.131592").json()
    return data

#convert JSON to dataframe
def convert_to_df():
    data = get_api()
    flatten_json = pd.json_normalize(data)
    df = pd.DataFrame.from_dict(flatten_json)
    return df  

#save dataframe to CSV
def store_to_csv():
    data = convert_to_df()
    csv_df = pd.DataFrame(data)
    csv_df.to_csv('/var/lib/mysql-files/police_street_crime.csv', index=False)
    return csv_df 

#declare default args
default_args = {
    'owner': 'airflow',
}

#set default args for dags
with DAG(
        dag_id='police_street_level_load_table',
        default_args=default_args,
        start_date=datetime(2025, 1, 21),
        tags=['police_dags']
    ) as dag:

    get_api_data = PythonOperator(
            task_id='get_api_data',
            python_callable=get_api,
            provide_context=True,
            dag=dag
        )
    convert_dataframe = PythonOperator(
            task_id='convert_dataframe',
            python_callable=convert_to_df,
            provide_context=True,
            dag=dag
    )
    save_to_csv = PythonOperator(
            task_id='save_to_csv',
            python_callable=store_to_csv,
            provide_context=True,
            dag=dag
        )

    #call sql script to create police_street_crime_table
    create_impt_police_street_crime = SQLExecuteQueryOperator(
            task_id='create_impt_police_street_crime',
            conn_id='airflow_db',
            sql="sql/impt_police_street_crime.sql",
            dag=dag
    )

    create_d_street_crime_category = SQLExecuteQueryOperator(
            task_id='create_d_street_crime_category',
            conn_id='airflow_db',
            sql="sql/d_street_crime_category.sql",
            dag=dag
    ),

    create_d_street_crime_location = SQLExecuteQueryOperator(
            task_id='create_d_street_crime_location',
            conn_id='airflow_db',
            sql="sql/d_street_crime_location.sql",
            dag=dag
    ),

    create_d_street_crime_outcome = SQLExecuteQueryOperator(
            task_id='create_d_street_crime_outcome',
            conn_id='airflow_db',
            sql="sql/d_street_crime_outcome.sql",
            dag=dag
    ),

    create_f_police_street_crime = SQLExecuteQueryOperator(
            task_id='create_f_police_street_crime',
            conn_id='airflow_db',
            sql="sql/f_police_street_crime.sql",
            dag=dag
    )

get_api_data >> convert_dataframe >> save_to_csv >> create_impt_police_street_crime

create_impt_police_street_crime >> create_d_street_crime_category
create_impt_police_street_crime >> create_d_street_crime_location
create_impt_police_street_crime >> create_d_street_crime_outcome

create_d_street_crime_category >> create_f_police_street_crime
create_d_street_crime_location >> create_f_police_street_crime
create_d_street_crime_outcome >> create_f_police_street_crime


#note doesn't like tuples with SQLExecute!
#task_start >> [create_impt_police_street_crime, create_d_street_crime_location, create_d_street_crime_outcome]





    

