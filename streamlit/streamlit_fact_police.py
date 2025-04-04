import streamlit as st
import pandas as pd
import os

#Load query
def load_query(filename):
    with open(os.path.join('sql_queries', filename), 'r') as f:
        return f.read()
    
#Load queries from SQL file
fact_query = load_query('fact.sql')

#Use loaded query
#Initialise connection
conn = st.connection('mysql', 'sql')
df = conn.query(fact_query, ttl=600)
st.table(df)