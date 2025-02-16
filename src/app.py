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
st.subheader("Plot Overview")
st.text('''The bar chart represents qualitative data about fruit sales, specifically comparing sales for four categories of fruits: Apple, Banana, Orange, and Grapes. The corresponding sales values for each fruit are provided as follows:
Apple: 30 units
Banana: 45 units
Orange: 20 units
Grapes: 25 units
The bar chart visualizes these values, where each bar represents a fruit, and the height of each bar reflects the number of sales for that fruit.''')
st.subheader("Interpretation of the Plot")
st.text('''1) Categories on the x-axis:
The x-axis shows the categories of fruits: Apple, Banana, Orange, and Grapes. These categories are qualitative in nature, meaning they represent different types of fruits without any inherent numerical order.

2) Values on the y-axis:
The y-axis represents the number of sales for each fruit, which is quantitative data. This axis measures the frequency or amount of sales corresponding to each fruit category.

3) Bars:
Each vertical bar represents the sales value for a specific fruit. The height of the bar corresponds to the number of sales for that particular fruit.
For example, the Banana bar is the tallest, showing that it has the highest sales (45), while Orange has the shortest bar, reflecting its lowest sales (20).

4) Color Palette:
The bars are colored using the "viridis" color palette from the seaborn library, which is known for its aesthetically pleasing gradient. The palette is used to distinguish the bars visually and make the chart more appealing. Each bar has a unique color, but the order remains consistent (as per the categories).''')
st.subheader("Advantages of a Bar Chart")
st.write('''1) Clarity:
Bar charts are excellent for comparing discrete categories. In this case, the sales of different fruits are easy to compare since the heights of the bars directly represent the sales numbers.
         
2) Visual Impact:
The use of colors helps to enhance the visual appeal of the chart, making it easier for users to focus on individual categories. The clear separation between the bars allows for quick recognition of differences in sales.

3) Quick Interpretation:
Bar charts allow viewers to quickly identify which category has the highest or lowest values. For example, it's easy to see that Banana has the highest sales, and Orange has the lowest.
         
4) Simplicity:
This is a simple and intuitive chart. It's easy to read and understand, making it suitable for presentations, reports, and basic data analysis.''')
st.subheader("Disadvantages of a Bar Chart")
st.write('''1) Limited Detail:
Bar charts provide a simple comparison but lack deeper insight into the data distribution. For example, we don't know the trend over time or the relationships between multiple variables (e.g., sales trends over months).

2) Limited for Large Datasets:
Bar charts work best for a small number of categories. As the number of categories grows (e.g., 20+ fruits), the chart can become cluttered and harder to interpret.

3) No Context for Differences:
The chart doesn't explain why certain fruits have higher or lower sales. To gain deeper insights, we would need additional information, such as seasonality, marketing efforts, or regional preferences.

4) Not Ideal for Continuous Data:
Bar charts are not suitable for representing continuous data (like temperatures or stock prices), as these datasets are better visualized using other charts such as line charts or histograms.''')
st.subheader("Conclusion")
st.write('''In this case, the bar chart effectively conveys the sales of four types of fruits. It allows for easy comparison between categories and visually represents the relative sales of apples, bananas, oranges, and grapes. However, it may not be the best choice for more complex datasets or when you need to convey deeper insights beyond simple comparisons.''')

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
