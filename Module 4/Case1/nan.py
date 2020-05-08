#Create a numpy array having NaN (Not a Number) and print it. array([ nan, 1., 2., nan, 3., 4., 5.])
#Print the same array omitting all elements which are nan
import numpy as np
A=np.asarray([ np.nan, 1., 2., np.nan, 3., 4., 5.])
print(A)
nan_array = np.isnan(A)
A = A[~nan_array]
print(A)
