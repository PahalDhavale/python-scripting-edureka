#By using list comprehension,
#please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].



lis1=[12,24,35,24,88,120,155]

lis2=[i for i in lis1 if i!=24]
print(lis2)
