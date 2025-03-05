#import dags, SQLOperator, Datetime
#from airflow.decorators import dag, task
from datetime import datetime, timedelta 
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow import DAG

#set the default args
default_args = {
    'owner': 'airflow',
}

#set default args for dags
dag = DAG(
        dag_id='simple_etl_dag',
        default_args=default_args,
        start_date=datetime(2025, 1, 21),
        tags=['example']
    )
    #call sql script to create sql table A
    #must use a sqloperator to run the sql script
create_main_tbl = SQLExecuteQueryOperator(
        task_id='create_main_tbl',
        conn_id='airflow_db',
        sql="sql/create_main_tbl.sql",
        dag=dag,
    )
        
    #call sql script to create sql table B containing rows to add
create_row_tbl = SQLExecuteQueryOperator(
        task_id='create_row_tbl',
        conn_id='airflow_db',
        sql="sql/create_row_tbl.sql",
        dag=dag,
    )

    #call sql script to add rows from table B to add to table A
add_rows = SQLExecuteQueryOperator(
        task_id='add_rows',
        conn_id='airflow_db',
        sql="sql/add_rows.sql",
        dag=dag,
    )
    #state dependencies (traditional)
create_main_tbl >> create_row_tbl >> add_rows



