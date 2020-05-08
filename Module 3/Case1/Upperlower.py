#Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
#Suppose the following input is supplied to the program: Hello world!
#Then, the output should be: UPPER CASE 1
#LOWER CASE 9

import re

string=input("String")

print ("UPPERCASE",len(re.findall(r'[A-Z]',string)))
print ("LowerCase",len(re.findall(r'[a-z]',string)))
