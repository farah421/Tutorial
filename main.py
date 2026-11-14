
import streamlit as st

st.set_page_config(
    page_title="DOSM Data Visualization",
    page_icon="📊",
    layout="wide"
)

st.title("DOSM Data Visualization Dashboard")

st.write("""
Welcome to the DOSM Data Visualization Dashboard.

This application presents data from three areas:
""")

st.markdown("""
### 1. Household Income
Explore household income inequality across districts in Malaysia.

### 2. Education
Explore school completion rates across districts in Malaysia.

### 3. Demographic
Explore annual live births across districts and sex in Malaysia.
""")

st.info("Select a page from the sidebar to explore the visualizations.")
