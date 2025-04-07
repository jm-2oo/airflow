import streamlit as st
import pandas as pd
import os

#Load query
def load_query(filename):
    with open(os.path.join('sql_queries', filename), 'r') as f:
        return f.read()
    
#Load queries from SQL file
fact_query = load_query('f_police_raw.sql')

#Use loaded query
#Initialise connection
conn = st.connection('mysql', 'sql')
df = conn.query(fact_query, ttl=600)

#Configure top text
st.title('Fact Table')
top_text = '''This is what the fact table looks in the data warehouse.  (-1 values means fact data couldn't join on to the dims).'''
st.markdown(top_text)

column_config={
    'category': st.column_config.TextColumn(width='medium')
}

st.dataframe(
    df,
    column_config=column_config,
    use_container_width=True, #configure text wrapping
    hide_index=True
)
