#!/bin/env python3
## A brief disclaimer, i made this code with help of Github Copilot, so it's not 100% mine, but i'm learning from it.
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('sales_data.csv')

# DATA EXPLORATION

## Display the first 5 rows of the DataFrame
print ("First 5 rows")
print (df.head(5))

## Check the shape of the DataFrame
print("Number of rows    : ", df.shape[0])
print("Number of columns : ", df.shape[1])

## Identify unique products
unique_products = df['ProductName'].unique()
print("Unique products   : ", unique_products)

# Data Filtering

## Display the first 5 rows of the filtered DataFrame
filtered_df = df[df['QuantitySold'] > 10]
print("Sales with QuantitySold greater than 10:")
print(filtered_df.head(5))

# Basic Analysis:

## Calculate total revenue
total_revenue = df['QuantitySold'] * df['Price']
print("Total revenue: ", total_revenue.sum())

## Find product with highest revenue
highest_revenue_product = df.loc[total_revenue.idxmax(), 'ProductName']
print("Product with highest revenue: ", highest_revenue_product)

# Visualization

## Get the top 5 products by QuantitySold
top_products = df.groupby('ProductName')['QuantitySold'].sum().nlargest(5)

## Create a bar chart
plt.bar(top_products.index, top_products.values)
plt.xlabel('Product')
plt.ylabel('QuantitySold')
plt.title('Top 5 Products by QuantitySold')

# Display the chart
plt.show()
