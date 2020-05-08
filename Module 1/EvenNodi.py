#3.Write a program, which will find all the numbers between 1000 and 3000 (both included) such that
#each digit of a number is an even number. The numbers obtained should be printed in a comma separated sequence on a single line.
#Hint: In case of input data being supplied to the question, it should be assumed to be a console input.
#Divide each digit with 2 and verify is it even or not.

#Finding Numbers between 1000 and 3000 , each digit of that number = even
import numpy as np

Numbers=[]

q = np.linspace(1000,3000,2001,dtype=int)
#q = [int(l) for l in q[0::2]]

z=[]

#print (list(z))
for i in q:
     z=list(str(i))
     if all(int(val) % 2 ==0 for val in z):
          Numbers.append(i)
            
     

print(Numbers)
