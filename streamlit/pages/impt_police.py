import streamlit as st
import pandas as pd
import os

#Load query
def load_query(filename):
    with open(os.path.join('sql_queries', filename), 'r') as f:
        return f.read()
    
#Load queries from SQL file
fact_query = load_query('impt_police.sql')

#Use loaded query
#Initialise connection
conn = st.connection('mysql', 'sql')
df = conn.query(fact_query, ttl=600)

#Configure text
st.title('Import Data')

top_text = 'Raw data comes from data.police.uk API: \nhttps://data.police.uk/api/crimes-street/all-crime?date=2024-01&lat=52.629729&lng=-1.131592'
st.markdown(top_text)

#Configure column and dataframe
column_config={
    'category': st.column_config.TextColumn(width='medium')
}

st.dataframe(
    df,
    column_config=column_config,
    use_container_width=True, #configure text wrapping
    hide_index=True
)
