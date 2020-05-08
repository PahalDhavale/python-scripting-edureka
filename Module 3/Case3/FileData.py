import re

File=open(r"C:\Users\Marx\Desktop\Python assignments\Converted\Bankdataset\777_m3_datasets_v1.0\FD.csv","r").read().splitlines()

Rep=[]
for i in range(0,len(File)):
     temp=File[i]
     Rep.append(temp.split(","))

Black=[]
White=[]
for i in range(len(Rep)):
     temp=Rep[i]
     temp1=re.sub(r"^\s+","",Rep[i][1],flags=re.UNICODE)
     temp1=re.sub(r"\s+$","",temp1,flags=re.UNICODE)
     temp1=re.sub(r"\s+", "",temp1, flags=re.UNICODE)
     if temp[2] == "1":
          Black.append(temp1)
     else:
          White.append(temp1)

Name=[]
for i in range(0,len(Rep)):
     string = Rep[i][1]
     temp1=re.sub(r"^\s+","",string,flags=re.UNICODE)
     temp1=re.sub(r"\s+$","",temp1,flags=re.UNICODE)
     Name.append(temp1)

parsed=[]
temp=[]
Name_Parsed=[]
for i in Name:
     temp=re.split('\s+',i)
     parsed.append(temp)
for i in parsed:
     Name_Parsed.append(''.join(i))

temp2={}
li=[]
for j in range(len(parsed)):
     if len(parsed[j]) > 2:
          temp2={"Title": parsed[j][0] , "First Name":parsed[j][1]  ,"Last Name":parsed[j][2]}
     else:
          temp2={"Title": parsed[j][0] , "First Name":parsed[j][1]  ,"Last Name":"Null"}
     li.append(temp2)

class Customer:
     
     def __init__(self):
          self.Data=li
          
     def data1(self):
          self.Data_Names=li
          self.Data_Rep=Rep
          self.Black_list=Black
          self.White_list=White
          for i in self.Data_Names:
               print(i)
          self.name_p=Name_Parsed

     def eligible(self,a):
          self.Data_Rep=Rep
          self.Data_Par=parsed
          self.Name_p=Name_Parsed
          self.Black_list=Black
          self.White_list=White
          try: 
               if a in self.Name_p:
                    print("Value present")
                    if a in self.Black_list:
                         raise CustomerNotAllowedException
                    else:
                      return("True")
               else:
                    print("Value is not present")
                    return("False")

          except CustomerNotAllowedException:
               print("Customer Blacklisted")

class Order():
     def __init__(self):
          self.Black_list=Black
          self.White_list=White

     def createOrder(self,a):         
          print("Customer can Order:")
          print("Enter Product Name")
          Product=input()
          print("Enter Product Code")
          ProductCode=input()
          OrderLi={"Customer Name":a, "Product Name":Product , "Product Code":ProductCode}
          print(OrderLi)
                   
Obj1=Customer()
Obj2=Order()

class Error(Exception):
     pass

class CustomerNotAllowedException(Error):
     pass

while True:
     quest=input("Do you Wish to view the customer list? Y or N ")
     if quest == "Y":
          Obj1.data1()
     print("\nEnter customer name to order eg: Mr. Harris")
     value1=input()
     print ("Checking Credibility of ",value1)
     temp1=re.sub(r"^\s+","",value1,flags=re.UNICODE)
     temp1=re.sub(r"\s+$","",temp1,flags=re.UNICODE)
     temp1=re.sub(r"\s+", "",temp1, flags=re.UNICODE)
     if Obj1.eligible(temp1) == "True":
          Obj2.createOrder(temp1)
     break









