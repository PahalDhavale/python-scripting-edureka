#write a program to randomly generate a list with 5 numbers
#which are divisible by 5 and 7 , between 1 and 1000 inclusive.


import numpy as np
'''
while True:
     ran=np.random.randint(1,1000,5)
     if ran%5==0 and ran %7 ==0:
          ranval.append(ran)
     if len(ranval) == 5:
          break
     

'''
arr = []
while True:
     ran = list(np.random.randint(1,1001,1))
     
     if int(ran[0])%5 == 0 and int(ran[0])%7 == 0:
          arr.append(ran[0])
     if len(arr) == 5:
          break
print(arr)
