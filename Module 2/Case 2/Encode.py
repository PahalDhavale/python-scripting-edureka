import numpy as np
from cryptography.fernet import Fernet

password = Fernet.generate_key() #this is your "password"
cipher_suite = Fernet(password)

#ReferenceId
Refid=input("Enter your reference Id")
encoding = "utf-8"
pk = bytes(Refid, encoding)
encoded_text = cipher_suite.encrypt(pk) 
decoded_text = cipher_suite.decrypt(encoded_text)



print(encoded_text)
print(decoded_text)

