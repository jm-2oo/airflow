#parllelisation works with python functions

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
        dag_id='police_parallel_test',
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
    
    ##################
    #empty task start
    task_start = BashOperator(
        task_id='start',
        bash_command='date'
    )

    #task_start >> [get_api_data, convert_dataframe]

    get_api_data >> [convert_dataframe, save_to_csv]