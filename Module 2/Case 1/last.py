#Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
#If the following n is given as input to the program: 5
#Then, the output of the program should be: 3.55

lis=int(input())
num=0
x=0
for x in range (1,lis+1):
     num=num+x/(x+1)

print (format(round(num,2)))
