#The aim of this project is to conduct exploratory data analysis on a provided dataset
# in order to acquire valuable insights and draw conclusions based on the data.

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('dataset.csv')

# Print the first few rows of the dataset
print(data.head())

# Determine the size of the dataset
print("Dataset dimensions:", data.shape)

# Identify the data types of each column
print(data.dtypes)

# Check for any missing values
print("Missing values:\n", data.isnull().sum())

# Calculate descriptive statistics
print("Descriptive statistics:\n", data.describe())

# Visualize a numeric variable with a histogram
plt.hist(data['numeric_variable'], bins=20)
plt.xlabel('Numeric Variable')
plt.ylabel('Frequency')
plt.title('Histogram: Numeric Variable')
plt.show()

# Plot a scatter plot of two numeric variables
plt.scatter(data['numeric_variable1'], data['numeric_variable2'])
plt.xlabel('Numeric Variable 1')
plt.ylabel('Numeric Variable 2')
plt.title('Scatter Plot: Numeric Variables')
plt.show()

# Create a bar chart for a categorical variable
data['categorical_variable'].value_counts().plot(kind='bar')
plt.xlabel('Categories')
plt.ylabel('Count')
plt.title('Bar Chart: Categorical Variable')
plt.show()
