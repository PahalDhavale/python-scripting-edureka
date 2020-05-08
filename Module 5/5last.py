#Draw a scatter graph of any 50 random values of x and y axis

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

x=np.random.randint(100,size=50)
y=np.random.randint(100,size=50)
colors = iter(cm.rainbow(np.linspace(0, 1, len(y))))
for i in y:
    plt.scatter(x, y, color=next(colors))
for i, txt in enumerate(x):
    plt.annotate(txt, (x[i], y[i]))
plt.show()

