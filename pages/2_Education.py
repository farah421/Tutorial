import streamlit as st
import pandas as pd
import plotly.express as px

st.title("School Completion Rates")

# Load cleaned dataset
df = pd.read_csv("data/school_completion.csv")

st.subheader("Objective 2")
st.write(
    "To analyse school completion rates across "
    "districts in Malaysia."
)

# Summary statistics
col1, col2, col3 = st.columns(3)

col1.metric("Total Records", len(df))
col2.metric("Number of Districts", df["district"].nunique())
col3.metric(
    "Average Completion Rate",
    f"{df['completion'].mean():.2f}"
)

# Summary
st.subheader("Summary")
st.info(
    "This page explores school completion rates "
    "by district, education stage and date."
)

# Filters
dates = sorted(df["date"].dropna().unique())
stages = sorted(df["stage"].dropna().unique())

selected_date = st.selectbox("Select Date", dates)
selected_stage = st.selectbox("Select Education Stage", stages)

filtered_df = df[
    (df["date"] == selected_date) &
    (df["stage"] == selected_stage)
]

# Visualization 1
st.subheader("Visualization 1: Completion Rate by District")

fig1 = px.bar(
    filtered_df.sort_values("completion", ascending=False),
    x="district",
    y="completion",
    title="School Completion Rate by District",
    labels={
        "district": "District",
        "completion": "Completion Rate"
    }
)

st.plotly_chart(fig1, use_container_width=True)

# Visualization 2
st.subheader("Visualization 2: Completion Rate Distribution")

fig2 = px.histogram(
    filtered_df,
    x="completion",
    nbins=15,
    title="Distribution of School Completion Rates",
    labels={"completion": "Completion Rate"}
)

st.plotly_chart(fig2, use_container_width=True)

# Visualization 3
st.subheader("Visualization 3: State Comparison")

state_df = (
    filtered_df.groupby("state", as_index=False)["completion"]
    .mean()
    .sort_values("completion", ascending=False)
)

fig3 = px.bar(
    state_df,
    x="state",
    y="completion",
    title="Average School Completion Rate by State",
    labels={
        "state": "State",
        "completion": "Average Completion Rate"
    }
)

st.plotly_chart(fig3, use_container_width=True)

# Interpretation
st.subheader("Data Interpretation")
st.write(
    "Compare completion rates between districts and states. "
    "Identify which districts have higher or lower completion "
    "rates for the selected education stage and date."
)
