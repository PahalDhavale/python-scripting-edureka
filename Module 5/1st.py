import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Load the data from the dataset into your program
File= pd.read_csv(r"C:\Users\Marx\Desktop\Python assignments\Executed Programs\Module 5\777_m5_datasets_v1.0\HU.csv")
print(File.to_string())

#plot a Bar Graph of the data
ax = File.plot(y='Hurricanes',x="Year",kind='bar', title ="Hurricanes", legend=True)
ax.set_ylabel("Year", fontsize=12)
ax.set_xlabel("Hurricanes", fontsize=12)
plt.show()
