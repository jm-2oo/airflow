from datetime import datetime, timedelta 
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow import DAG

#set the default args
default_args = {
    'owner': 'airflow',
}

#set default args for dags
dag = DAG(
        dag_id='fruits_dag',
        default_args=default_args,
        start_date=datetime(2025, 1, 21),
        tags=['example']
    )
    #call sql script to create fruits table and load csv file
create_fruits_tbl = SQLExecuteQueryOperator(
        task_id='create_fruits_tbl',
        conn_id='airflow_db',
        sql="sql/create_fruits_tbl.sql",
        dag=dag,
    )