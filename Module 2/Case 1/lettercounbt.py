#Write a program which count and print the numbers of each character in a string input by console.
#Example: If the following string is given as input to the program: abcdefgabc

string=input()
string1=set(string)
string1=sorted(string1,key=string.index)
for i in string1:
     print(i,string.count(i))
     
