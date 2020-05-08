#Read the three csv files which contains the score of same students in term1 for each Subject
#MathScoreTerm1.csv DSScoreTerm1.csv, PhysicsScoreTerm1.csv
import numpy as np
import pandas as pd

Math=pd.read_csv(r"C:\Users\Marx\Desktop\Python assignments\Executed Programs\Module 4\M4set\MathScoreTerm1.csv")
DSS=pd.read_csv(r"C:\Users\Marx\Desktop\Python assignments\Executed Programs\Module 4\M4set\DSScoreTerm1.csv")
Phys=pd.read_csv(r"C:\Users\Marx\Desktop\Python assignments\Executed Programs\Module 4\M4set\PhysicsScoreTerm1.csv")

#Remove the name and ethnicity column (to ensure confidentiality)
Drop=['Ethinicity','Name']
Math.drop(Drop,axis=1,inplace=True)
DSS.drop(Drop,axis=1,inplace=True)
Phys.drop(Drop,axis=1,inplace=True)

#Fill missing score data with zero
Math['Score'].fillna(0,inplace=True)
DSS['Score'].fillna(0,inplace=True)
Phys['Score'].fillna(0,inplace=True)

#print((Math['Score'].isnull()).to_string())

#Merge the three files
Score=pd.concat([Math,DSS,Phys])

#Change Sex(M/F) Column to 1/2 for further analysis
Score['Sex'].replace(to_replace ="M" , value = 1,inplace=True)  
Score['Sex'].replace(to_replace ="F" , value = 2,inplace=True)

#Store the data in new file – ScoreFinal.csv
Score.to_csv(r"C:\Users\Marx\Desktop\Python assignments\Executed Programs\Module 4\ScoreFinal.csv")

#Enchancements 

Math1=pd.read_csv(r"C:\Users\Marx\Desktop\Python assignments\Executed Programs\Module 4\M4set\MathScoreTerm1.csv")
DSS1=pd.read_csv(r"C:\Users\Marx\Desktop\Python assignments\Executed Programs\Module 4\M4set\DSScoreTerm1.csv")
Phys1=pd.read_csv(r"C:\Users\Marx\Desktop\Python assignments\Executed Programs\Module 4\M4set\PhysicsScoreTerm1.csv")

#Convert ethnicity to numerical value

#print(Math1['Ethinicity'].unique())
li=[Math1,DSS1,Phys1]
for i in li:
     i['Ethinicity'].replace(to_replace ='White American' , value = 1,inplace=True)
     i['Ethinicity'].replace(to_replace ='European American' , value = 2,inplace=True)
     i['Ethinicity'].replace(to_replace ='Hispanic' , value = 3,inplace=True)
     i['Ethinicity'].replace(to_replace ='African American' , value = 4,inplace=True)

#Fill the missing score for a student to the average of the class
Math1['Score'].fillna(Math1['Score'].mean(),inplace=True)
DSS1['Score'].fillna(DSS1['Score'].mean(),inplace=True)
Phys1['Score'].fillna(Phys1['Score'].mean(),inplace=True)




