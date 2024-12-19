# Exploratory Data Analysis (EDA) for Marvel vs DC

### Importing necessary libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset

data = pd.read_csv('CSV/Marvel_DC.csv')

# Data Cleaning and Preprocessing

# 1. Normalization of Year

# Extracted the year using regular expressions and converted to numeric values

data['Year'] = data['Year'].astype(str).str.extract(r'(\d{4})').astype(float)
data['Year'] = data['Year'].fillna(data['Year'].median())

# 2. Transformation of RunTime

# Extracted numeric values from the runtime column using regular expressions and converted to numeric values

data['RunTime'] = data['RunTime'].astype(str).str.extract(r'(\d+)').astype(float)
data['RunTime'] = data['RunTime'].fillna(data['RunTime'].median())

# 3. Handling Missing Values

# Replaced missing values in the Genre column with the string 'Unknown'

data['Genre'] = data['Genre'].fillna('Unknown')

# Exploratory Analysis

# Univariate Analysis

# Distribution of IMDb Scores (Histogram)

plt.figure(figsize=(10, 6))
sns.histplot(data['IMDB_Score'], bins=20, kde=True)
plt.title('Distribution of IMDb Scores')
plt.xlabel('IMDb Score')
plt.ylabel('Frequency')
plt.show()

# Bivariate Analysis

# Relationship Between Genres and IMDb Scores (Boxplot)

plt.figure(figsize=(12, 8))
sns.boxplot(x='Genre', y='IMDB_Score', data=data)
plt.title('IMDb Scores by Genre')
plt.xlabel('Genre')
plt.ylabel('IMDb Score')
plt.xticks(rotation=90)
plt.show()

# Results

# Marvel vs DC IMDb Ratings Comparison

marvel_movies = data[data['Franchise'] == 'Marvel']
dc_movies = data[data['Franchise'] == 'DC']

# Average IMDb Score

marvel_avg_score = marvel_movies['IMDB_Score'].mean()
dc_avg_score = dc_movies['IMDB_Score'].mean()

print(f"Marvel Average IMDb Score: {marvel_avg_score}")
print(f"DC Average IMDb Score: {dc_avg_score}")

# Common Genres (Top 5)

common_genres = data['Genre'].value_counts().head(5)
print("Top 5 Common Genres:")
print(common_genres)

# Correlation between RunTime and IMDb Score

runtime_corr = data[['RunTime', 'IMDB_Score']].corr()
print("Correlation between RunTime and IMDb Score:")
print(runtime_corr)

# Tools Used

# - pandas for data manipulation.

# - numpy for numerical operations.

# - matplotlib and seaborn for data visualization.

# How to Run

# 1. Clone the repository.

# 2. Place the Marvel_DC.csv file in the src/data/ directory.

# 3. Run the Jupyter Notebook containing the EDA code.

# Future Work

# - Analyze additional variables such as budget and revenue to understand their impact on success.

# - Perform sentiment analysis on reviews to gain more insights.
