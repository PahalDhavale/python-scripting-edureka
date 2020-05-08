import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.pyplot import figure
figure(num=None, figsize=(4, 5), dpi=100, facecolor='w', edgecolor='k')
x = np.array([1,2,3,4])
y = np.array([20, 21, 20.5, 20.8])
# 5.1 Draw a Simple plot, 5.3 Configure the axes
plt.plot(x,y,label='X VS Y',c='black',ls ='-',lw=2,dash_capstyle='round',marker='D', ms=5)
#  5.4 Give title of Graph & labels of x axis and y axis
plt.xlabel("X",fontsize=20)
plt.ylabel("Y",fontsize=20)
plt.legend()
plt.show()
# Configure the line and markers in simple plot
markerindex = np.random.randint(0, len(Line2D.markers), 4)
figure(num=None, figsize=(4, 5), dpi=100)
for k,m in enumerate (Line2D.markers):
     i = (markerindex == k)
     plt.scatter(x[i],y[i],marker=m)
y_error = [0.12, 0.13, 0.2, 0.1]
plt.errorbar(x,y,yerr=y_error, linestyle="None")
plt.xlabel("X",fontsize=20)
plt.ylabel("Y",fontsize=20)
plt.legend()
plt.show()
