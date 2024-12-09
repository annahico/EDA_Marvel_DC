import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load data
data = pd.read_csv('src/data/films.csv')

# Clean data
data.dropna(inplace=True)

# Exploratory analysis
print(data.describe())
sns.histplot(data['budget'])
plt.show()
