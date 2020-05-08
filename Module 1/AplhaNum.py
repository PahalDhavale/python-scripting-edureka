#Write a program that accepts a sentence and calculate the number of letters and digits.
#Suppose if the entered string is: Python0325 Then the output will be:
#LETTERS: 6 DIGITS:4
#Hint: Use built-in functions of string.


#Acceptin a sentence
sent=input()
#Calculating number of letters
alp=0
dig=0
sent1=list(sent)
print(sent1)
for i in sent1:
     if   (i.isalpha()):
                alp += 1
     elif(i.isdigit()):
               dig=dig+1
print ("Letters",alp,"Digits",dig)
