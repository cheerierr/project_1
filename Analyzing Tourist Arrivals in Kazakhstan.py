import pandas as pd
import matplotlib.pyplot as plt

# Load the tourist arrival dataset
data = pd.read_csv('tourist_arrivals_kazakhstan.csv')

# Print the first few rows of the dataset
print(data.head())

# Check the dimensions of the dataset
print("Dataset dimensions:", data.shape)

# Check for any missing values
print("Missing values:\n", data.isnull().sum())

# Calculate total tourist arrivals by region
region_totals = data.groupby('Region')['Tourist Arrivals'].sum().sort_values(ascending=False)

# Plot a bar chart of tourist arrivals by region
plt.figure(figsize=(10, 6))
region_totals.plot(kind='bar')
plt.xlabel('Region')
plt.ylabel('Total Tourist Arrivals')
plt.title('Tourist Arrivals by Region in Kazakhstan')
plt.xticks(rotation=45)
plt.show()
