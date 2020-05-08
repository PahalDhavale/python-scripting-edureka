#A website requires a user to input username and password to register.
#Write a program to check the validity of password given by user.
#Following are the criteria for checking password:
#	1.	At least 1 letter between [a-z]
#        2.	At least 1 number between [0-9]
#	3. At least 1 letter between [A-Z]
#	4. At least 1 character from [$#@]
#	5. Minimum length of transaction password: 6
#	6. Maximum length of transaction password: 12


import re

username=input("Enter username")
password=input("Enter password")

#Checking with regex
#[a-z][0-9][A-Z][$#@] len6 Pass1

#\w ->[a-zA-Z0-9_]
if re.match(r"[\w$#@]{6,12}",password):
     print("Password OK")
else:
     print("wromg pass form")
     

               

