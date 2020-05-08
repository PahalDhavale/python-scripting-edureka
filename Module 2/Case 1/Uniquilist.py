#With a given list [12,24,35,24,88,120,155,88,120,155],
#write a program to print this list after removing all duplicate values with original order reserved.



lis1=[12,24,35,24,88,120,155,88,120,155]

lis1=list(dict.fromkeys(lis1))
print (lis1[::-1])

