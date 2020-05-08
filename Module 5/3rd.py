#Plot a pie-chart of the number of models released by every manufacturer,
#recorded in the data provide. Also mention the name of the manufacture with the largest releases.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re

File=pd.read_csv(r"C:\Users\Marx\Desktop\Python assignments\Executed Programs\Module 5\777_m5_datasets_v1.0\Cars.csv")
A1=np.asarray(File['Make'])
A=list()
for i in range(len(A1)):
     str=re.sub(r'\s+$','',A1[i])
     A.append(str)
unique,counts=np.unique(A,return_counts=True)
A=list(zip(unique,counts))
Man=list()
Num=list()
for i in range(len(A)):
     Man.append(A[i][0])
     Num.append(A[i][1])
Max=max(Num)
for i in range(len(A)):
     if A[i][1] == Max:
          MaxStr="Highest Release ",A[i]
plt.title(MaxStr)
plt.pie(Num,labels=Man)
plt.show()

