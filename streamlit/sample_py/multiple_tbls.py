import streamlit as st
import pandas as pd
import os

#Load query
def load_query(filename):
    with open(os.path.join('sql_queries', filename), 'r') as f:
        return f.read()
    
#Load queries from SQL file
sql_query1 = load_query('d_street_crime_category.sql')
sql_query2 = load_query('d_street_crime_location.sql')

conn = st.connection('mysql', 'sql')

table1 = conn.query(sql_query1, ttl="10m")
table2 = conn.query(sql_query2, ttl="10m")

#Configure columns for each table
category_config={
        'd_street_crime_category_ID': st.column_config.TextColumn('d_street_crime_category_ID', width='small'),
        'street_crime_category': st.column_config.TextColumn('street_crime_category', width='medium')
        }

# Display tables
st.header("Table 1")
st.dataframe(
    table1,
    column_config=category_config, #use 'category_config' variable here
    use_container_width=True, #configure text wrapping
    hide_index=True, #hide df index
    height=None
)

st.header("Table 2")
st.dataframe(table2)