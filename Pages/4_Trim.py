import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv("E:/AI/Notebooks/car_prices.csv")
st.header("Insights of Trims")
st.markdown("Trim: A designation within a model that indicates specific features or options (e.g., LX, EX, XLE)")
has_models_column = "trim" in df.columns

# User input for selecting interest (assuming the column exists)
interest_options = ["year", "condition", "odometer", "mmr", "sellingprice"]
interest = st.sidebar.selectbox("Select Your Interest", interest_options)


if has_models_column:
    mydf = df.nlargest(10, interest)
    st.plotly_chart(px.bar(mydf, x="trim", y=interest, title=f"Top 10 {interest}"), use_container_width=True)
else:
    st.write("The 'trim' column is not available in the dataset.")
st.header(f"Line scatter of {interest}")
fig_scatter = px.scatter(df, x='trim', y=interest)
st.plotly_chart(fig_scatter, use_container_width=True)

if df[interest].dtype == "object":
  st.header(f"Distribution of Cars by {interest}")
  fig_pie = px.pie(df, names=interest, values=df.groupby(interest)['trim'].count().reset_index()['trim'])  # Count cars by interest category
  st.plotly_chart(fig_pie, use_container_width=True)
else:
  st.write(f"Pie chart not suitable for continuous Y-axis ({interest}).")

st.dataframe(df)


max_value = df[interest].max()
min_value = df[interest].min()
avg_value = round(df[interest].mean(), 1)

col1, col2, col3 = st.columns(3)
col1.metric(label=f"Max {interest}", value=max_value)
col2.metric(label=f"Min {interest}", value=min_value)
col3.metric(label=f"Avg {interest}", value=avg_value)


col1.markdown(f'<h2 style="text-align: center; color: #191970 ;">Top 10 {interest}</h2>', unsafe_allow_html=True)
top_df = df.nlargest(10, interest)
col1.dataframe(top_df)

col2.markdown(f'<h2 style="text-align: center; color: #191970 ;">Bottom 10 {interest}</h2>', unsafe_allow_html=True)
bottom_df = df.nsmallest(10, interest)
col2.dataframe(bottom_df)