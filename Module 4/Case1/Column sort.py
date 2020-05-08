#Create a random matrix and Compute a matrix rank.
import numpy as np

Ar=np.random.randint(10,size=9).reshape(3,3)
print(Ar)
print(np.linalg.matrix_rank(Ar))
