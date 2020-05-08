#Design a software for bank system.
#There should be options like cash withdraw, cash credit and change password.
#According to user input, the software should provide required output.
#Hint: Use if else statements and functions.



def cash_with(self):
     print("Withdrawing Cash, avlb =",self)
     amt1=int(input("Enter Amt."))
     return(self-amt1)

def cash_cre(self):
    print("Cash credit, bal =", self)
    amt2=int(input("Enter amy being credited"))
    return(self+amt2)

def chg_pas(self):
     print("Password Change")
     newp=input("Enter new pass")
     if newp != self :
          return(newp)
     else:
          print("pass same")
          exit 
amt=1000
pas="abc"

while True:
     action=int(input("Enter the action to  perform : \n 1. Withdraw \n 2. Credit \n 3. Pass \n 4. Exit "))
     
     if action == 1:
          amt=cash_with(amt)
     elif action == 2:
          amt=cash_cre(amt)
     elif action == 3:
          pas=chg_pas(pas)
     elif action == 4:
          print ("Current Bal is: ",amt)
          break



