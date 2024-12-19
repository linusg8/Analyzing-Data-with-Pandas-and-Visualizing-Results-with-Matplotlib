import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
file_path = 'business-financial-data-sep-2024-quarter-csv.csv'  
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(data.head())
# Basic information about the dataset
data.info()

# Summary statistics
data.describe()
# Check for missing values
print(data.isnull().sum())



# Drop rows with missing values (if necessary)
data.dropna(inplace=True)



# Visualizing Results with Matplotlib
# Line plot


plt.plot(data['Data_value'], data['Period'] , label='Line ')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title(' Plot in VS Code')
plt.show()
# Scatter plot
plt.scatter(data['Period'], data['Data_value'])
plt.title('Scatter Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
plt.plot(data['Period'], data['Data_value'])
plt.title('bar')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

plt.plot(x, y, label='Line Example')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Sample Plot in VS Code')
plt.show()