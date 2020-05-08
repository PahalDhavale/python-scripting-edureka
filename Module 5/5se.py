import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
seaborn.set(style='ticks')

#Create a dataframe from following data

df = pd.DataFrame({
'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'], 'female': [0, 1, 1, 0, 1],
'age': [42, 52, 36, 24, 73],
'preTestScore': [4, 24, 31, 2, 3],
'postTestScore': [25, 94, 57, 62, 70]
})
Val=[0,1]

#Draw a Scatterplot of preTestScore and postTestScore, with the size of each point determined by age

plt.scatter(df['preTestScore'],df['postTestScore'],s=df['age']*2)
plt.show()


#data in question 9 of preTestScore and postTestScore with the size = 300 and the color determined by sex

fg = seaborn.FacetGrid(data=df, hue='female', hue_order=Val, aspect=1.61)
fg.map(plt.scatter,'preTestScore', 'postTestScore',s=300).add_legend()
plt.show()
