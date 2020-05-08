#Data of XYZ company is stored in sorted list. Write a program for searching specific data from that list.
#Hint: Use if/elif to deal with conditions.


#Storing ID's in a list

id= [144,232,4223,14,63,77,134,567]
id = sorted(id)

Search=int(input("Enter the id \t"))

for i in range (len(id)):
     if id[i] == Search:
          print ("Id present at position:", i)
     elif id != i:
          print("id not present at position:",i)
