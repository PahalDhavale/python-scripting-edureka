#Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H]
#Following are the fixed values of C and H: C is 50. H is 30.
#D is the variable whose values should be input to your program in a comma- separated sequence.
#Let us assume the following comma separated input sequence is given to the program:
#100,150,180
#The output of the program should be:
#18,22,24
import math
from math import sqrt

values=input("Enter Comma seprated values").split(",")
print(values)
Q=[]
for i in values:
     Q.append((int(math.sqrt((100 * int(i)  )/30))))
print (*Q,sep=",")
