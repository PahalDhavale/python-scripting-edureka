#1.	Write a program which will find factors of given number and find whether the factor is even or odd.

#using for loops

FaNum=input()
Fac=set()

for i in range(1,int(FaNum)-int(1)):
    for j in range (1,int(FaNum)-int(1)):
        if i*j == int(FaNum):
            Fac.update([i,j])
        else:
            continue
print(Fac)
