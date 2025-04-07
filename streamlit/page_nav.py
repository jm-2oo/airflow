import streamlit as st

# Define pages with custom titles
intro_page = st.Page("pages/intro.py", title="Intro", icon="✨")
page_1 = st.Page("pages/report_tbl_police.py", title="Report Table", icon="✨")
page_2 = st.Page("pages/fact_police.py", title="Fact Table", icon="✨")
page_3 = st.Page("pages/dim_police.py", title="Dim Tables", icon="✨")
page_4 = st.Page("pages/impt_police.py", title="Import Table", icon="✨")

# Create navigation
pg = st.navigation([intro_page, page_1, page_2, page_3, page_4])
pg.run()