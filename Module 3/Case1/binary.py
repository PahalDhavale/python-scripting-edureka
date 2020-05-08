#Write a program which accepts a sequence of comma separated 4 digit binary numbers
#as its input and then check whether #they are divisible by 5 or not.
#The numbers that are divisible by 5 are to be printed in a comma separated sequence.
 
binary=input("Input 4 digit binaries , seprated").split(",")
binc=[]
for x in binary:
     try:
          if int(x,2) and len(x) > 3:
               binc.append(int(x))
     except ValueError:
          continue
     
deci=[]
for i in binc:
     dec=0
     for x in str(i):
          dec=dec*2+ int(x)
     deci.append(int(dec))
     
decid=[]
for i in deci:
     if i % 5 == 0:
          decid.append(bin(i).replace("0b", ""))
print(''.join(decid))





          
