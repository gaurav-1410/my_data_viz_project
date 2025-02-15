import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

st.title("Qualitative & Quantitative Data Visualization")

# Qualitative Data
categories = ["Apple", "Banana", "Orange", "Grapes"]
values = [30, 45, 20, 25]

st.subheader("Qualitative Data (Fruit Sales)")
df_qual = pd.DataFrame({"Category": categories, "Sales": values})
st.write(df_qual)  # Display the data in a table

# Bar Chart
st.subheader("Bar Chart (Qualitative Data)")
fig, ax = plt.subplots()
ax.bar(categories, values, color=sns.color_palette("viridis", len(categories)))
ax.set_title("Fruit Sales Bar Chart")
st.pyplot(fig)

# Pie Chart
st.subheader("Pie Chart (Qualitative Data)")
fig, ax = plt.subplots()
ax.pie(values, labels=categories, autopct='%1.1f%%', colors=sns.color_palette("pastel"))
st.pyplot(fig)

# Quantitative Data
np.random.seed(42)
heights = np.random.normal(loc=170, scale=10, size=100)

st.subheader("Quantitative Data (Student Heights)")
df_quant = pd.DataFrame({"Heights (cm)": heights})
st.write(df_quant)  # Display the data in a table

# Histogram
st.subheader("Histogram (Quantitative Data)")
fig, ax = plt.subplots()
sns.histplot(heights, bins=10, kde=True, color="blue", ax=ax)
st.pyplot(fig)

# Box Plot
st.subheader("Box Plot (Quantitative Data)")
fig, ax = plt.subplots()
sns.boxplot(y=heights, color="orange", ax=ax)
st.pyplot(fig)

# ECDF Plot
st.subheader("ECDF (Quantitative Data: Student Heights)")
fig, ax = plt.subplots()
sns.ecdfplot(heights, color="green", ax=ax)
ax.set_title("Empirical Cumulative Distribution Function (ECDF) of Student Heights")
st.pyplot(fig)

# Scatter Plot Data
np.random.seed(42)
hours_studied = np.random.randint(1, 10, 50)
exam_scores = hours_studied * 10 + np.random.randint(-5, 5, 50)

st.subheader("Quantitative Data (Hours Studied vs Exam Scores)")
df_scatter = pd.DataFrame({"Hours Studied": hours_studied, "Exam Scores": exam_scores})
st.write(df_scatter)  # Display the data in a table

# Scatter Plot
st.subheader("Scatter Plot (Quantitative Data)")
fig, ax = plt.subplots()
sns.scatterplot(x=hours_studied, y=exam_scores, color="red", ax=ax)
st.pyplot(fig)

st.write("This app displays visualizations for both qualitative and quantitative data.")
