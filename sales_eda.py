import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("customer_sales.csv")
print("First 5 rows:")
df.head()
print("\nDataset Info:")
df.info()
print("\nStatistical Summary:")
df.describe()
print("\nMissing Values:")
df.isnull().sum()
df.dtypes
# EDA Analysis
# Region-wise Sales Analysis
region_sales = df.groupby("Region")["Sales"].sum()
print(region_sales)
#Top Products by Sales
product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print(product_sales)
# Gender-wise Profit Analysis
gender_profit = df.groupby("Gender")["Profit"].sum()
print(gender_profit)

# Data Visulization
# Region-wise Sales Bar Chart
region_sales.plot(kind="bar")
plt.title=("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

# Top Products (Bar Chart)
product_sales.head(5).plot(kind="bar")
plt.title=("Top 5 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

# Profit Distribution(Histogram Chart)
df["Profit"].plot(kind="hist")
plt.title=("Profit Distribution")
plt.xlabel("Profit")
plt.show()

print("\nEDA Completed Successfully!")