#example of working mysql connection
import streamlit as st
import pandas as pd

# Initialize connection.
conn = st.connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * FROM f_police_street_crime WHERE 	FK_street_crime_outcome_statusID <> -1 LIMIT 10;', ttl=600)

# Print results.
st.table(df)