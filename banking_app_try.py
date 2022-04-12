accountno = " "
customerName = " "
Bankcode = " "
mobile = " "
ifsc = ""
email= ""
def createAccount( ):
      accountNo = int(input("enter account number: "))
      customerName = input("enter name: ")
      Bankcode = input("enter bankcode: ")
      mobile = int(input("enter mobile number: "))
      ifsc= input("Enter the IFSC code: ")
      email=input("Enter customer email id: ")

def showAcntDetails ( ):
      print("AccountNO:",accountno)
      print("customerName:",customerName)
      print("Bankcode:",Bankcode)
      print("mobile:",mobile)
      print("IFSC Code: ",ifsc)
      print("Customer Email ID: ",email)


#function#
cont=input("Enter 'Yes' if you want to continue else hit enter:")
while cont:
      print("1.create account\n 2.withdraw\n 3.deposit\n 4.check balance\n 5.show account details")
      choose=int(input("select the above option"))
      if (choose==1):
            createAccount( )
            print("Account created successfully")
      elif(choose==2):
            amnt=int(input("enter the amount to withdraw"))
            withdraw(amnt)
      elif(choose==3):
            amnt=int(input("enter the amount to deposit"))
            deposit(amnt)
      elif(choose==4):
            chckbalance( )
      elif(choose==5):
            showAcntDetails()
      else:
            print("select the above options available")
      cont = input("Enter 'Yes' if you want to continue else hit enter:")



