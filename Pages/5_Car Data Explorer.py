import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv('E:/AI/Notebooks/car_prices.csv')  # Replace with your data file path

st.header("Exploring Car Distribution by Make, Model, Seller, and Trim (Specific and descriptive)")

st.markdown("""
This page provides a comprehensive overview of the car data, allowing you to explore the various makes, models, sellers, and trims available in the dataset. 

Here, you can gain insights into:

* The types of cars being sold
* The distribution of models across different sellers
* The prevalence of specific trims within each model

Feel free to use the sorting and filtering options (if available) to refine your exploration and focus on specific aspects of the data.

**Key Data Points:**

* Make: Manufacturer of the car (e.g., Ford, Kia, Chevrolet)
* Model: Specific car model (e.g., Sorento, F-150, Camry)
* Seller: The entity selling the car (e.g., Kia Motors America Inc, Enterprise Vehicle Exchange)
* Trim: A designation within a model that indicates specific features or options (e.g., LX, EX, XLE)
""")

feature_options = df.columns.tolist()


def remove_selected(options, selected):
  """Removes the selected feature from the available options list."""
  return [option for option in options if option != selected]


st.sidebar.header("Select Features")
selected_feature_x = st.sidebar.selectbox("X-axis Feature", feature_options.copy())
feature_options_without_x = remove_selected(feature_options.copy(), selected_feature_x)
selected_feature_y = st.sidebar.selectbox("Y-axis Feature", feature_options_without_x)


st.header(f"Descriptive Plot of {selected_feature_x} with {selected_feature_y}")
fig_Scatter = px.scatter(df, x=selected_feature_x, y=selected_feature_y)
st.plotly_chart(fig_Scatter, use_container_width=True)

if df[selected_feature_y].dtype == "object":
  st.header(f"Distribution of {selected_feature_x} by {selected_feature_y}")
  fig_pie = px.pie(df, names=selected_feature_y, values=selected_feature_x)
  st.plotly_chart(fig_pie, use_container_width=True)
else:
  st.write(f"Pie chart not suitable for continuous Y-axis ({selected_feature_y}).")
