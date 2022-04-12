a=""
b=""
def add():
    return a+b
def sub():
    return a-b
def mul(a,b):
    return  a*b
def div(a,b):
    return a/b
def rem(a,b):
    return a%b

number1=float(input('Enter the first value: '))
number2=float(input('Enter the second value: '))

print("""Options for calculator operations 
1. Addition
2. Subtractoion
3. Multiplication
4. Division
5.Remider
""")

choice=int(input("Enter the choice of arithmatic oprtation you want to perform on your given values: "))

if (choice==1):
    print(add(number1,number2))
elif (choice==2):
    print(sub(number1,number2))
elif (choice==3):
    print(mul(number1,number2))
elif(choice==4):
    print(div(number1,number2))
    """quo=div(number1,number2)
    if quo<=1:
        print("Blue")
    else:
        print("Black")  ---> These statements are for the practice"""

elif(choice==5):
    print(rem(number1,number2))
    colour=rem(number1,number2)
    if colour==1:
        print("Blue")
    else:
        print("Black")
else:
    print("You're a default danny choose correct option")



