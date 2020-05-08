import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Reading Data

File=pd.read_csv(r"C:\Users\Marx\Desktop\Python assignments\Executed Programs\Module 5\Dataset.csv")
print(File.to_string())

#Describe the data Describe the data on the unit price

print(File.describe())
print(File[['unit price']].describe())

#Create new dataframe having columns 'name','net_price','date' and group all the records according to name

A=File[['name','net_price','date']]
B=A.groupby('name')
print(B.groups)

C=B['net_price'].sum()

ax=C.plot(kind='bar')
for p in ax.patches:
     ax.annotate("%.2f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points')
plt.setp(ax.get_xticklabels(), rotation=40, horizontalalignment='right')
plt.show()


