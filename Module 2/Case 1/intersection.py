#With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155],
#write a program to make a list whose elements are intersection of the above given lists.


lis1=[1,3,6,78,35,55]
lis2=[12,24,35,24,88,120,155]

seta=set(lis1)
setb=set(lis2)
lisint=[]
lisint=seta & setb

print ( lisint)
