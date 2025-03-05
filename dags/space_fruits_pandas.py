from datetime import datetime, timedelta 
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow import DAG
from airflow.decorators import task 
from airflow.operators.python import PythonOperator

import requests
import json
import pandas as pd
import csv 

#get api data csv file
def get_api_csv():
    data = ()
#transform file
#load to csv
#load to db table