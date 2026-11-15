
import streamlit as st
import pandas as pd
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="DOSM Data Visualization",
    page_icon="📊",
    layout="wide"
)

# Dashboard title
st.title("DOSM Data Visualization Dashboard")
st.write("Data visualization using Department of Statistics Malaysia (DOSM) datasets.")

# Data folder location
DATA_DIR = Path(__file__).parent / "data"

# Load datasets
@st.cache_data
def load_data():
    income = pd.read_csv(DATA_DIR / "household_income_cleaned.csv")
    education = pd.read_csv(DATA_DIR / "school_completion_cleaned.csv")
    births = pd.read_csv(DATA_DIR / "annual_live_birth_cleaned.csv")

    # Clean column names
    income.columns = income.columns.str.strip().str.lower()
    education.columns = education.columns.str.strip().str.lower()
    births.columns = births.columns.str.strip().str.lower()

    return income, education, births

# Display datasets
try:
    income, education, births = load_data()

    st.success("All 3 datasets loaded successfully!")

    st.subheader("Dataset Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Household Income", f"{len(income):,} records")
    col2.metric("Education", f"{len(education):,} records")
    col3.metric("Live Births", f"{len(births):,} records")

    # Dataset preview
    st.subheader("Dataset Preview")

    tab1, tab2, tab3 = st.tabs([
        "Household Income",
        "Education",
        "Live Births"
    ])

    with tab1:
        st.dataframe(income.head(10), use_container_width=True)

    with tab2:
        st.dataframe(education.head(10), use_container_width=True)

    with tab3:
        st.dataframe(births.head(10), use_container_width=True)

except FileNotFoundError as e:
    st.error(f"CSV file not found: {e}")
    st.info("Please check that all three CSV files are inside the data folder.")

except Exception as e:
    st.error(f"Something went wrong: {e}")
