#The dataset given, records data of city temperatures over the years 2014 and 2015.
#Plot the histogram of the temperatures over this period for the cities of San Francisco and Moscow.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

File=pd.read_csv(r"C:\Users\Marx\Desktop\Python assignments\Executed Programs\Module 5\777_m5_datasets_v1.0\CT.csv")
print(File)

Drop=['Month','Melbourne','Year']
File.drop(Drop,axis=1,inplace=True)

colors = ['red','green']
layer=['Moscow','San']
plt.hist([File['Moscow'],File['San Francisco']],color=colors,label=layer,bins=range(-10,25),stacked=True)
plt.legend(prop={'size': 10})
plt.show()


