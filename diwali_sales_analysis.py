# -*- coding: utf-8 -*-
"""Diwali Sales Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jpeKz52xVV7FvSEoo8aX5Wp5McI6dR7X
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

"""Importing Data"""

from google.colab import files
uploaded = files.upload()

df = pd.read_csv("Diwali_Sales_Data.csv", encoding = "unicode_escape")

df.shape

df.head(13)

"""Data Cleaning


"""

df.info()

del(df["Status"])

del(df["unnamed1"])

#finding number of null values column wise
df.isna().sum()

#dropping null value rows
df.dropna(inplace = True)

#changing datatype of a column
df["Amount"] = df["Amount"].astype(int)

#rename column
df.rename(columns = {"Marital_Status":"shadi"})

"""Data Analysis"""

# gender wise number of orders
sns.countplot(x = "Gender", data = df)

#gender wise sales amount
sales_gen = df.groupby("Gender").sum("Amount").sort_values(by = "Amount", ascending = False)
sns.barplot(x = "Gender",y = "Amount",data = sales_gen)

# clustered column chart of age group and gender wise number of records
sns.countplot(x = "Age Group", hue = "Gender", data = df)

#top 10 states according to sales amount
top10states = df.groupby("State").sum("Amount").sort_values(by = "Amount", ascending = False).head(10)
sns.set(rc ={"figure.figsize": (18,5)})
sns.barplot(x= "State", y = "Amount", data = top10states)

# Number of Orders wrt to Marital Status
sns.set(rc = {"figure.figsize": (5,5)})
ax = sns.countplot(x= "Marital_Status", data = df)
for bars in ax.containers:
  ax.bar_label(bars)

# top 5 occupations according to Sales Amount
top5occupation = df.groupby("Occupation").sum("Amount").sort_values(by = "Amount", ascending = False).head(5)
sns.set(rc = {"figure.figsize":(12,5)})
tr = sns.barplot(x = "Occupation", y = "Amount", data = top5occupation)

# no of orders wrt to product category
qw = sns.countplot(x= "Product_Category", data = df)
sns.set(rc = {"figure.figsize":(10,5)})
for bars in qw.containers:
  qw.bar_label(bars)

# top 5 most sold products
top5products = df.groupby("Product_ID").sum("Orders").sort_values(by = "Orders", ascending = False).head(5)
sns.barplot(x = "Product_ID", y = "Orders", data = top5products)

"""Conclusion

Some major points from analysis are :
1) Females places more orders than males.And sales amount wise also their contribution is more than males.
2) Females between age group 26-35 place highest number of orders
3) Uttar Pradesh, Maharashtra, Karnataka, Delhi, Madhya Pradesh have highest contribution of sales.
4) Non married people orders more than married people.
5) IT sector, healthcare, aviation, banking, governemnt contribute highes sales amount.
"""