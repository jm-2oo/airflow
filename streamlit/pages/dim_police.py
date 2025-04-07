import streamlit as st
import pandas as pd
import os

#Load query
def load_query(filename):
    with open(os.path.join('sql_queries', filename), 'r') as f:
        return f.read()
    
#Load table queries from SQL file
sql_query1 = load_query('d_street_crime_category.sql')
sql_query2 = load_query('d_street_crime_location.sql')
sql_query3 = load_query('d_street_crime_outcome.sql')

#SQL connection
conn = st.connection('mysql', 'sql')
table1 = conn.query(sql_query1, ttl=600)
table2 = conn.query(sql_query2, ttl=600)
table3 = conn.query(sql_query3, ttl=600)

#Configure top text
st.title('Dim Tables')

top_text = 'The dimension tables are split into: Street Crime Category; Street Crime Location and Street Crime Outcome.'
st.markdown(top_text)

#Display Tables
#Convert tables to Dataframe ie. df = 'table1'
st.header('d_street_crime_category')
st.dataframe(
    table1,
    use_container_width=True, #configure text wrapping
    hide_index=True, #hide df index
    height=None
)

st.header('d_street_crime_location')
st.dataframe(
    table2,
    use_container_width=True, #configure text wrapping
    hide_index=True, #hide df index
    height=None
)

st.header('d_street_crime_outcome')
st.dataframe(
    table3,
    use_container_width=True, #configure text wrapping
    hide_index=True #hide df index
)