#Read the data in pandas data frame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
#matplotlib.pyplot.scatter
File=pd.read_csv(r"C:\Users\Marx\Desktop\Python assignments\Executed Programs\Module 4\M4set\MS.csv")
print("Describing the File : \n \n ",File.describe())
print("File Info \n \n \n :",File.info())

#Group data by school ratings
Temp=File[["school_rating","reduced_lunch"]]
Mean=Temp.groupby(["school_rating"], as_index=False).mean()
print("Mean Value : \n \n \n ",Mean)

#Correlation analysis
print("Correlation Analysis \n \n \n \n",File[["school_rating","reduced_lunch"]].corr(method='pearson'))

#plt.scatter(File["school_rating"],File["reduced_lunch"])
#Scatter Plot
File.plot.scatter(y='school_rating',x='reduced_lunch',c='DarkBlue',style='o')
plt.show()

#Correlation Matrix
corr=File.corr(method='pearson')
corr.style.background_gradient(cmap='coolwarm')
sn.heatmap(corr, annot=True)
plt.show()
