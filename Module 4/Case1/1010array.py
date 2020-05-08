#Create a 10x10 array with random values and find the minimum and maximum values.
import numpy as np

A=np.random.randint(100,size=(100)).reshape(10,10)
print(A)
print(np.amax(A))          
print(np.amin(A))
