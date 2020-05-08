#Checking if a string is palinderom or not

stmt=input()
revst=''.join(reversed(stmt))
if (stmt == revst):
     print("pali")
else:
     print("not palind")
