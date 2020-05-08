#Create a numpy array [[0, 1, 2], [ 3, 4, 5], [ 6, 7, 8],[ 9, 10, 11]]) and filter the elements greater than 5.

import numpy as np

Ar=np.asarray([[0, 1, 2], [ 3, 4, 5], [ 6, 7, 8],[ 9, 10, 11]])
print(Ar)
Ar = Ar[Ar < 5]
print(Ar)
