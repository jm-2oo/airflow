import streamlit as st
import pandas as pd
import os

#Load query
def load_query(filename):
    with open(os.path.join('sql_queries', filename), 'r') as f:
        return f.read()
    
#Load queries from SQL file
sql_query = load_query('report_tbl_police.sql')

#Use loaded query
#Initialise connection
conn = st.connection('mysql', 'sql')
df = conn.query(sql_query, ttl=600)

st.title('Reporting Table')
top_text = ('This is sample of what the table would look like for further processing in a report.')
st.markdown(top_text)

column_config={
        'street_crime_case_id': st.column_config.TextColumn('Case ID', width='small'),
        'location_name': st.column_config.TextColumn('Location', width='medium'),
        'street_crime_category': st.column_config.TextColumn('Crime Category', width='medium'),
        'street_crime_outcome': st.column_config.TextColumn('Case Outcome', width='large')
    }

st.dataframe(
    df,
    column_config=column_config,
    use_container_width=True, #configure text wrapping
    hide_index=True #hide df index
)
