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
st.subheader("What is the Histogram Showing?")
st.write('''In this case, the histogram is plotting the distribution of student heights based on the randomly generated data. Here's a breakdown of the elements in the plot:

1) Data Generation:
You are generating 100 random student heights using a normal distribution (np.random.normal) with the following parameters:
Mean (loc) = 170 cm: This is the average height of the students.
Standard Deviation (scale) = 10 cm: This represents how much variation or spread there is around the mean height. A larger standard deviation would mean a wider spread of heights around the average.
Size (size) = 100: This means you are generating 100 random student heights.

2) Histogram:
The x-axis represents the height range in centimeters.
The y-axis represents the frequency or count of students who fall within each height range (i.e., the number of students whose heights lie within each bin).
The bars in the histogram represent the count of students within a specific range of heights (called a bin). For example, one bin could represent the range of 160-165 cm, and the height of the bar tells you how many students fall within that range.

3) KDE (Kernel Density Estimate):
On top of the histogram, a smooth curve (represented by the KDE) is drawn. The KDE gives a smooth estimate of the distribution of the data, making it easier to visualize the overall shape of the data and where it is most concentrated.

4) Bins:
The histogram is divided into 10 bins, as indicated by the bins=10 parameter. This means the data is split into 10 equal intervals along the x-axis (height), and each bar corresponds to the frequency of students falling within that interval.''')
st.subheader("Detailed Explanation of the Graph")
st.write('''1) Distribution: The histogram shows that the student heights are normally distributed, meaning they follow a bell-shaped curve (as we set the distribution to normal with a mean of 170 and standard deviation of 10). The KDE curve is also bell-shaped, reinforcing this idea.

2) Central Tendency: The highest frequency (tallest bar) will likely be around the mean value (170 cm), indicating that most students' heights are close to this value. This confirms that 170 cm is the most common height in the dataset.

3) Spread: The spread of the heights is determined by the standard deviation. Since the standard deviation is 10 cm, most of the students' heights will fall within the range of 160 cm to 180 cm. The farther you go from this range, the fewer students you will encounter.

4) Skewness: In this case, the histogram is expected to be fairly symmetrical, meaning there is no skewness in the data. If the bars skew to the left or right, it would suggest that more students are either shorter or taller than the average height.''')
st.subheader("Conclusions that Can Be Drawn from the Graph")
st.write('''1) Most students have heights close to the average (170 cm). The highest concentration of students falls in the range of around 160 cm to 180 cm. This is expected for any normally distributed data.

2) Outliers are rare: There are few students whose heights fall far outside the typical range (either much shorter or much taller than the average). This indicates that the data is tightly clustered around the mean.

3) Symmetry of the distribution: The histogram is likely symmetrical, indicating the data follows a normal distribution. If there was a noticeable skew (left or right), it would suggest that the student heights are not normally distributed.

4) Variation in student heights: The histogram gives us a clear sense of the spread of the data. In this case, most students' heights vary within a range of approximately 160 cm to 180 cm, which is within one standard deviation from the mean (170 cm).''')
st.subheader("Usefulness of the Histogram")
st.write('''Histograms like this one are highly useful in several scenarios:

1) Understanding the Distribution: Histograms allow you to quickly assess the distribution of data. For example, in this case, it shows us that the student heights follow a normal distribution with a specific mean and standard deviation. This helps in understanding the underlying data trends.

2) Detecting Outliers: If there were any extreme values (outliers) in the dataset, they would appear as isolated bars far from the peak. This can be useful for identifying anomalies or mistakes in data collection.

3) Comparison of Different Datasets: If you had multiple datasets (e.g., student heights from different schools or cities), histograms could help you compare their distributions. For instance, if one school had a much larger average height, that would show up as a histogram shifted to the right.

4) Predictive Modeling: Knowing the distribution of a dataset helps in choosing appropriate statistical or machine learning models. For instance, if you know your data is normally distributed, you might choose models or methods that work well with that type of data (e.g., linear regression).

5) Assessing the Spread of Data: The histogram shows the spread of data, which is critical when making decisions about variance, standard deviation, and other statistical measures.''')
st.subheader("Information the Graph Tells Us")
st.write('''1) Most students' heights are concentrated around the average height (170 cm).
2) Height distribution is symmetric and follows a normal distribution.
3) The spread of student heights is limited, with most students falling within the 160 cm to 180 cm range.
4) Fewer extreme heights are observed, indicating that there are no significant outliers in the data.''')
st.subheader("Limitations and Considerations")
st.write('''1) Bin Selection: The choice of bins can impact the interpretation of the histogram. Too few bins can make the data appear too generalized, while too many bins can create a noisy and fragmented view of the data.

2) Skewed Data: In cases where the data is not normally distributed (e.g., if the data has a long tail or is skewed), a histogram can still be useful, but it may require adjustments to the binning strategy or transformation of the data for more accurate analysis.''')
st.subheader("Conclusion")
st.write('''In summary, the histogram for student heights provides valuable insight into the distribution of the data, helping us understand the central tendency, spread, and shape of the distribution. This visualization is useful for assessing the normality of the data, detecting outliers, and understanding how heights are distributed in a population.''')

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
