import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
rs = np.random.RandomState(0)
df = pd.DataFrame(rs.rand(10, 10))
corr = df.corr()
corr.style.background_gradient(cmap='coolwarm')
plt.show()
