#!!this works
#save api data to csv#

from datetime import datetime, timedelta 
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow import DAG
from airflow.decorators import task 
from airflow.operators.python import PythonOperator

import requests
import json
import pandas as pd
import csv 


def get_api():
    data = requests.get("http://api.open-notify.org/astros").json()
    return data 

def store_to_csv():
    data = get_api()
    df = pd.DataFrame(data)
    df.to_csv('/var/lib/mysql-files/api_py_table_load.csv', index=False)
    return df 

#declare default args
default_args = {
    'owner': 'airflow',
}

#set default args for dags
with DAG(
        dag_id='space_fruits_load_table',
        default_args=default_args,
        start_date=datetime(2025, 1, 21),
        tags=['current_dags']
    ) as dag:

    get_api_data = PythonOperator(
            task_id='transform_user',
            python_callable=get_api,
            provide_context=True,
            dag=dag,
        )
    save_csv = PythonOperator(
            task_id='save_csv_id',
            python_callable=store_to_csv,
            provide_context=True,
            dag=dag
        )
    #call sql script to create space_fruits table and load csv file
    create_fruits_tbl = SQLExecuteQueryOperator(
        task_id='create_fruits_tbl',
        conn_id='airflow_db',
        sql="sql/space_fruits.sql",
        dag=dag,
    )
    
get_api_data >> save_csv >> create_fruits_tbl