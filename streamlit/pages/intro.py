import streamlit as st
from PIL import Image

st.title('Intro')
top_text = '''Hello and welcome to my Streamlit page.

This is where you can see table samples my MySQL database where I extracted data from data.police.uk API.   

I used Airflow to orchestrate the ETL process and to transform the tables for further processing in reports.

GitHub link: https://github.com/jm-2oo/airflow'''

st.markdown(top_text)

st.subheader('Architecture diagram of the ETL process:')
image = Image.open('police_architecture.png')
st.image(image, caption='Architecture diagram', output_format='PNG', width=800)

st.subheader('Conceptual model of the police data:')
image = Image.open('police_conceptual.png')
st.image(image, caption='Police data conceptual model', width=400)