accountno = " "
customerName = " "
Bankcode = " "
mobile = " "
ifsc = ""
email= ""
amount= ""
def createAccount( ):
      accountno = int(input("enter account number: "))
      customerName = input("enter name: ")
      Bankcode = input("enter bankcode: ")
      mobile = int(input("enter mobile number: "))
      ifsc= input("Enter the IFSC code: ")
      email=input("Enter customer email id: ")

def withdraw():
      amount = int(input("enter the amount to withdraw : "))
      print(f"Amount {amount} withdrawn ")

def deposit():
      amount=int(input("Enter the amount that needed to be deposited : "))
      print(f"{amount} is deposited into your account")

def checkbalance():
      print("Balance in your account")

#def showAcntDetails ( ):
      #print("AccountNO:",accountno)
      #print("customerName:",customerName)
      #print("Bankcode:",Bankcode)
      #print("mobile:",mobile)
      #print("IFSC Code: ",ifsc)
      #print("Customer Email ID: ",email)


#Calling the functions into the if and else loops#

print(" 1.create account\n 2.withdraw\n 3.deposit\n 4.check balance\n 5.show account details")
choose=int(input("select the above option :"))

if (choose==1):
      createAccount( )
elif(choose==2):
      withdraw()
elif(choose==3):
     deposit()
elif(choose==4):
      checkbalance( )
#elif(choose==5):
      #showAcntDetails()
else:
      print("select the above options available")

print("Thanks for using our services")
