#2.	Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically.

word=input()
word=list(word)
fword=sorted(word)
print (''.join(fword))
