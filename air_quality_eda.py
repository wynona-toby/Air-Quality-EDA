# -*- coding: utf-8 -*-
"""Air Quality EDA

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1c4pRvFYFagvbeCvgxbdGOkm_0xCLo6Yu

# **Agenda For Data Set [Air Quality]**
1. **Data Introduction**: Overview of the air quality dataset and its features (pollutants, weather). Analyze pollution patterns across cities and identify factors contributing to higher pollution levels.
2. **Data Description & Summary**: Structure, statistics, missing data, and anomalies.
3. **Data Cleaning**: Handle missing values, convert data types, and preprocess.
4. **Data Visualization**: Explore distributions, trends, and correlations using plots.
5. **Overall Status**: Summarize key insights and pollutant levels by city.
6. **Conclusion**: Highlight actionable findings and next steps.

# **1. Data Introduction**
"""

#Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Import Data
df = pd.read_csv("/content/global_air_quality_data_10000.csv")
print(df.head())

df.info()

"""The Global Air Quality Data dataset contains 10,000 records of air quality measurements from major cities worldwide, offering valuable insights into various environmental indicators. Each entry includes data on pollutants such as PM2.5, PM10, NO2, SO2, CO, and O3, along with meteorological conditions like temperature, humidity, and wind speed.

Dataset Analysis :

No. of records : 10,000

No. of Attributes : 10

No of Independent variables : 10

# 1.1 Data Preprocessing and Cleaning
"""

# Check for missing values
missing_values = df.isnull().sum()
print(missing_values)
# Check for duplicates
duplicates = df.duplicated().sum()
print(duplicates)

"""NO MISSING VALUE OR DUPLICATES"""

df['Date'] = pd.to_datetime(df['Date'])

# Fill missing numerical data with mean values and ignore non-numeric column
numeric_columns = df.select_dtypes(include=[np.number]).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# Check if missing values are filled
print("Missing Values After Filling:\n", df.isnull().sum())
print(df.head())

"""Dataset has been Cleaned and Preprocessed

# **2. Data Description and Summary**

# 2.1 Data Description
"""

print("Data Description:\n", df.describe())

"""# 2.2 Data Summary

This dataset contains air quality measurements across different cities
worldwide, focusing on various pollutants and weather conditions. The key attributes in the dataset are:

- City: Name of the city where the data was recorded.
- Country: The country of the city.
- Date: The date of air quality recording.
- PM2.5: Fine particulate matter smaller than 2.5 micrometers.
- PM10: Particulate matter smaller than 10 micrometers.
- NO2: Nitrogen dioxide concentration.
- SO2: Sulfur dioxide concentration.
- CO: Carbon monoxide concentration.
- O3: Ozone concentration.
- Temperature: Temperature in degrees Celsius.
- Humidity: Percentage of humidity.
- Wind Speed: Speed of wind in meters per second.

# **3. Data Analysis**

# 3.1 Grouping by Cities and getting average pollutant levels
"""

pollutant_means = df.groupby('City')[['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3']].mean()

pollutant_means.plot(kind='bar', figsize=(10, 6))
plt.title("Average Pollutant Levels by City")
plt.ylabel("Average Concentration")
plt.xlabel("City")
plt.xticks(rotation=45)
plt.legend(title="Pollutants")
plt.show()

"""# 3.2 Correlation analysis between pollutants and environmental factors

"""

numeric_columns = ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3', 'Temperature', 'Humidity', 'Wind Speed']
corr_matrix = df[numeric_columns].corr()

plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Between Pollutants and Environmental Factors")
plt.show()

"""# 3.3 Analysis of highest pollutant levels per city


"""

max_pollutants = df.groupby('City')[['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3']].max()

max_pollutants.plot(kind='bar', figsize=(10, 6))
plt.title("Maximum Pollutant Levels by City")
plt.ylabel("Maximum Concentration")
plt.xlabel("City")
plt.xticks(rotation=45)
plt.legend(title="Pollutants")
plt.show()

"""# CITY COMPARISONS"""

import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
plt.style.use('ggplot')
columns_to_analyze = ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3', 'Temperature', 'Humidity', 'Wind Speed']

fig = go.Figure()

# Add histograms
for column in columns_to_analyze:
    fig.add_trace(go.Histogram(
        x=df[column],
        name=column,
        opacity=0.75,
        histnorm='density',
        marker=dict(line=dict(width=0.5)),
    ))

# Update layout
fig.update_layout(
    title='Distribution of Pollutants and Meteorological Data',
    xaxis_title='Value',
    yaxis_title='Density',
    barmode='overlay',
    bargap=0.1,
    template='plotly_white'
)

# Show the plot
fig.show()

"""# **4. Data Visualization**

# 4.1 Histogram for pollutant distribution
"""

plt.figure(figsize=(10, 6))
df[['PM2.5', 'PM10', 'NO2', 'SO2', 'CO']].hist(bins=10, figsize=(12, 8), layout=(2, 3))
plt.suptitle('Distribution of Pollutants', fontsize=16)
plt.show()

"""# 4.2 Heatmap of correlations between pollutants and weather conditions"""

plt.figure(figsize=(10, 6))
corr = df[['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3', 'Temperature', 'Humidity', 'Wind Speed']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

"""# 4.3 Bar plot for average pollutant levels by city"""

pollutant_columns = ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3', 'Temperature', 'Humidity', 'Wind Speed']
df[pollutant_columns] = df[pollutant_columns].apply(pd.to_numeric, errors='coerce')
city_group = df.groupby('City')[pollutant_columns].mean()
plt.figure(figsize=(10, 6))
city_group[['PM2.5', 'PM10', 'NO2', 'SO2', 'CO']].plot(kind='bar')
plt.title('Average Pollutant Levels by City')
plt.ylabel('Concentration')
plt.xticks(rotation=45)
plt.show()

"""# 4.4 Scatterplot of NO2 vs PM2.5 Conc."""

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='PM2.5', y='NO2', hue='City', style='City', s=100)
plt.title('Scatter Plot of PM2.5 vs NO2 Levels')
plt.xlabel('PM2.5 Concentration')
plt.ylabel('NO2 Concentration')
plt.legend(title='City')
plt.show()

"""# 4.5 BoxPlot of PM2.5 vs City


"""

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='City', y='PM2.5', palette='Set2')
plt.title('Box Plot of PM2.5 Levels by City')
plt.ylabel('PM2.5 Concentration')
plt.xlabel('City')
plt.xticks(rotation=45)
plt.show()

"""# **5. Summary and Conclusion**

# 5.1 Overal Summary

The analysis of the air quality dataset reveals critical insights into the pollutant levels across various cities. Using statistical and visual techniques, we were able to:

1. **Identify Pollution Levels**:
   - Average pollutant levels (PM2.5, PM10, NO2, SO2, CO) were calculated for each city, revealing significant disparities in air quality.
2. **Explore Relationships**:
   - Scatter plots were used to examine correlations between pollutants, such as PM2.5 and NO2, demonstrating that these pollutants often rise and fall together.
3. **Assess Environmental Factors**:
   - Correlations between pollutants and environmental factors like temperature and humidity were evaluated, revealing low correlations overall, suggesting other factors may influence pollution levels.

# 5.2 Conclusion

The findings underscore the urgent need for targeted air quality management and pollution control strategies, especially in cities with higher pollutant levels. Key conclusions drawn from the analysis include:

1. **High Pollution Levels**: Cities such as **Bangkok** and **Rio de Janeiro** face significant air quality challenges, particularly concerning PM2.5 and NO2 levels, which can have serious health impacts.

2. **Pollutant Relationships**: There is a notable correlation between certain pollutants, indicating that efforts to reduce one pollutant may positively affect others.

In summary, this analysis highlights the importance of ongoing monitoring and evaluation of air quality to mitigate health risks associated with air pollution and emphasizes the need for comprehensive strategies to combat pollution in urban areas.
"""