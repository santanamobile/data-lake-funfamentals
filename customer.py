#!/bin/env python3
## A brief disclaimer, i made this code with help of Github Copilot, so it's not 100% mine, but i'm learning from it.
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('customer_data.csv')

# DATA EXPLORATION

## Display the first 5 rows of the DataFrame
print ("First 5 rows")
print (df.head(5))

## Total number of rows and columns 
print("Number of rows    : ", df.shape[0])
print("Number of columns : ", df.shape[1])

## Identify unique customers and products
unique_customers = df['CustomerID'].unique()
unique_products = df['ProductID'].unique()
print("Unique customers  : ", unique_customers)
print("Unique products   : ", unique_products)

# Customer Segmentation:
## Create a new DataFrame containing only female customers
female_customers = df[df['Gender'] == 'Female']
## Calculate the average age of male and female customers separately
average_age_male = df[df['Gender'] == 'Male']['Age'].mean()
average_age_female = female_customers['Age'].mean()

# Basic Analysis:
## Calculate and display the total purchase amount in the dataset
total_purchase_amount = df['PurchaseAmount'].sum()
print("Total purchase amount: ", total_purchase_amount)
## Identify the most purchased product.
most_purchased_product = df['ProductID'].value_counts().idxmax()
print("Most purchased product: ", most_purchased_product)

# Age Group Analysis (Optional):
## Create age groups
df['AgeGroup'] = pd.cut(df['Age'], bins=[18, 25, 35, 45, 55, 65], labels=['18-25', '26-35', '36-45', '46-55', '56-65'])
## Analyze average purchase amount for each age group
average_purchase_amount_by_age_group = df.groupby('AgeGroup')['PurchaseAmount'].mean()
print("Average purchase amount by age group:")
print(average_purchase_amount_by_age_group)
## Omit the NaN values
average_purchase_amount_by_age_group = average_purchase_amount_by_age_group.dropna()
## Sort ascending
average_purchase_amount_by_age_group = average_purchase_amount_by_age_group.sort_values(ascending=True)
## Visualize the results using a bar chart
average_purchase_amount_by_age_group.plot(kind='bar', color='skyblue')
plt.xlabel('Age Group')
plt.ylabel('Average Purchase Amount')
plt.title('Average Purchase Amount by Age Group')
plt.show()
