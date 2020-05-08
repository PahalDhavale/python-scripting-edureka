import re

File1= open(r"C:\Users\Marx\Desktop\Python assignments\Converted\Bankdataset\777_m3_datasets_v1.0\bank-data.csv","r")

File2=File1.readlines()
line_count=0
List_file=[]
for i in range(1,len(File2)):
     temp=File2[i]
     List_file.append(temp.split(","))

Prof=[]
for i in range(len(List_file)):
     a=List_file[i][1]
     if a not in Prof:
          Prof.append(a)
Age=[]
for i in range(len(List_file)):
     a=List_file[i][0]
     b=List_file[i][3]
     b=b.replace('\n','')
     if a not in Age and b == "yes":
          Age.append(a)

Limit={"Max":max(Age),"Min":min(Age)}
print(Limit)

Eligible=[]
for i in range(len(List_file)):
     a=List_file[i][3]
     a=a.replace('\n','')
     b=List_file[i][1]
     if a == "yes" and b not in Eligible:
          Eligible.append(b)
        
while True:
     Action1=input("Enter the Profession to search Eligibility \n").lower()
     if re.match(r'^[a-zA-Z]+$',Action1):
          print("Valid Input")
          Action=Action1
     aag_check=input("Enter the Age to search Eligibility\n")
     if re.match(r'[0-9]',aag_check):
               print("Valid Input")
               aag=aag_check
     if Action in Prof and aag in Age:
          print ("Entered profession and age is \n",Action, aag)
          if Action in Eligible and aag in Age:
               print("Loan Eligiblity: YES")
          else:
               print("Loan Eligibility: NO")
     else:
          print("No profession in list")
          break
File1.close()



