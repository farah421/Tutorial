import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Annual Live Birth by District and Sex")

# Load cleaned dataset
df = pd.read_csv("data/annual_live_birth.csv")

st.subheader("Objective 3")
st.write(
    "To analyse annual live births across districts "
    "in Malaysia according to sex."
)

# Summary statistics
col1, col2, col3 = st.columns(3)

col1.metric("Total Records", len(df))
col2.metric("Number of Districts", df["district"].nunique())
col3.metric("Total Live Births", f"{df['abs'].sum():,}")

# Summary
st.subheader("Summary")
st.info(
    "This page explores annual live births by district "
    "and sex using the number of births recorded."
)

# Date filter
dates = sorted(df["date"].dropna().unique())
selected_date = st.selectbox("Select Date", dates)

filtered_df = df[df["date"] == selected_date]

# Visualization 1
st.subheader("Visualization 1: Live Births by District")

district_df = (
    filtered_df.groupby("district", as_index=False)["abs"]
    .sum()
    .sort_values("abs", ascending=False)
)

fig1 = px.bar(
    district_df,
    x="district",
    y="abs",
    title="Total Live Births by District",
    labels={"district": "District", "abs": "Number of Births"}
)

st.plotly_chart(fig1, use_container_width=True)

# Visualization 2
st.subheader("Visualization 2: Live Births by Sex")

sex_df = (
    filtered_df.groupby("sex", as_index=False)["abs"]
    .sum()
)

fig2 = px.pie(
    sex_df,
    names="sex",
    values="abs",
    title="Distribution of Live Births by Sex",
    hole=0.4
)

st.plotly_chart(fig2, use_container_width=True)

# Visualization 3
st.subheader("Visualization 3: Live Birth Trends")

trend_df = (
    df.groupby(["date", "sex"], as_index=False)["abs"]
    .sum()
)

fig3 = px.line(
    trend_df,
    x="date",
    y="abs",
    color="sex",
    markers=True,
    title="Live Birth Trends by Sex",
    labels={"date": "Date", "abs": "Number of Births"}
)

st.plotly_chart(fig3, use_container_width=True)

# Interpretation
st.subheader("Data Interpretation")
st.write(
    "Compare the number of live births across districts "
    "and between sexes. The trend chart helps identify "
    "changes in recorded live births over time."
)
