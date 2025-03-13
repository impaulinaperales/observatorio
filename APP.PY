
import streamlit as st 
import pandas as pd 

st.set_page_config(layout="wide")

df = pd.read_csv("/Users/paulinaperales/Desktop/airbnb.csv")
st.title("Airbnb Data")
st.dataframe(df.head())

df_host = df.groupby(["host_id", "host_name"]).size().reset_index()
df_host_sorted = df_host.sort_values(by=0, ascending=False).head(10)
st.subheader("Top Hosts in Madrid")

st.dataframe(df_host_sorted)

import plotly.express as px
fig = px.bar(df_host_sorted, x="host_name", y=0, title="Top Hosts in Madrid")
st.plotly_chart(fig)

# Select top Hosts

host_selection = st.radio("How many hosts do you want to visualize?", [5, 10, 15, 20, 50])
st.dataframe(df_host.sort_values(by=0, ascending=False).head(host_selection))
