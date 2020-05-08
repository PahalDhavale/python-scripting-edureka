#1.Extract data from the given SalaryGender CSV file and store the data from each column in a separate NumPy array

import numpy as np
import pandas as pd

#File1=open(r"C:\Users\Marx\Desktop\Python assignments\Executed Programs\Module 4\M4set\SG.csv").read()
#print(File1,"\n")
FileNum=np.genfromtxt(r"C:\Users\Marx\Desktop\Python assignments\Executed Programs\Module 4\M4set\SG.csv", delimiter=",", names=True)

FileNum.dtype.names
salary=FileNum['Salary']
gender=FileNum['Gender']
age=FileNum['Age']
phd=FileNum['PhD']
countMen=0
countWen=0
for i in range(len(age)):
     if gender[i] == 1 and phd[i] == 1:
          countMen=countMen+1
     elif gender[1] == 0 and phd[i] == 1:
          countWen=countWen+1
     else:
          continue
#print ("Men With Phd",countMen, " Women with Phd",countWen)
     

#2.	Find:The number of men with a PhD , The number of women with a PhD
df=pd.read_csv(r"C:\Users\Marx\Desktop\Python assignments\Executed Programs\Module 4\M4set\SG.csv")
df1 = df[df.PhD != 0]
Var1=df1['Gender'].value_counts()
#print("Women With pHd",Var1[0],"Men with phd",Var1[1])



#3.Store the “Age” and “PhD” columns in one DataFrame and delete the data of all people who don’t have a PhD from SalaryGender CSV file.

df2=df1.iloc[:,[2,3]]
print(df2.head())

print(df2['PhD'].value_counts())
















