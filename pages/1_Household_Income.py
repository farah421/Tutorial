import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Household Income Inequality")

# Load cleaned dataset
df = pd.read_csv("data/household_income.csv")

st.subheader("Objective 1")
st.write(
    "To analyse household income inequality "
    "across districts in Malaysia."
)

# Summary statistics
col1, col2, col3 = st.columns(3)

col1.metric("Total Records", len(df))
col2.metric("Number of Districts", df["district"].nunique())
col3.metric("Average Gini Index", round(df["gini"].mean(), 3))

st.subheader("Summary")
st.info(
    "This page explores household income inequality "
    "using the Gini index across Malaysian districts."
)

# Select date
dates = sorted(df["date"].dropna().unique())
selected_date = st.selectbox("Select Date", dates)

filtered_df = df[df["date"] == selected_date]

# Visualization 1
st.subheader("Visualization 1: Gini Index by District")

fig1 = px.bar(
    filtered_df,
    x="district",
    y="gini",
    title="Household Income Inequality by District",
    labels={"district": "District", "gini": "Gini Index"}
)

st.plotly_chart(fig1, use_container_width=True)

# Visualization 2
st.subheader("Visualization 2: Gini Index Distribution")

fig2 = px.histogram(
    filtered_df,
    x="gini",
    nbins=15,
    title="Distribution of Gini Index",
    labels={"gini": "Gini Index"}
)

st.plotly_chart(fig2, use_container_width=True)

# Visualization 3
st.subheader("Visualization 3: State Comparison")

state_df = (
    filtered_df.groupby("state", as_index=False)["gini"]
    .mean()
    .sort_values("gini", ascending=False)
)

fig3 = px.bar(
    state_df,
    x="state",
    y="gini",
    title="Average Gini Index by State",
    labels={"state": "State", "gini": "Average Gini Index"}
)

st.plotly_chart(fig3, use_container_width=True)

st.subheader("Data Interpretation")
st.write(
    "Use the visualizations to compare inequality levels "
    "between districts and states and identify differences "
    "in the distribution of Gini index values."
)
