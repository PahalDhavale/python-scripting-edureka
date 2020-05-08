#Write a program which can compute the factorial of a given numbers. Use recursion to find it.
#Hint: Suppose the following input is supplied to the program:

def fac(self):
     if self<1 or self==0:
          return 1
     else:
          return self * fac(self -1)

print (fac(8))
