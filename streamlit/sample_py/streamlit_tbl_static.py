import streamlit as st
import pandas as pd
import os

#Load query
def load_query(filename):
    with open(os.path.join('sql_queries', filename), 'r') as f:
        return f.read()
    
#Load queries from SQL file
fact_query = load_query('fact_police.sql')

#Use loaded query
#Initialise connection
conn = st.connection('mysql', 'sql')
df = conn.query(fact_query, ttl=600)

st.title('Fact Table - Streamlit Static Table Sample')
st.table(df)

# Define pages with custom titles
main_page = st.Page("streamlit_fact_police_static.py", title="Main Page", icon="🎈")
page_2 = st.Page("pages/streamlit_fact_police_df_tbl.py", title="Page 2", icon="🎈")

# Create navigation
pg = st.navigation([main_page, page_2])
pg.run()