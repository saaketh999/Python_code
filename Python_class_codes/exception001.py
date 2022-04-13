num1=int(input("Enter the First number :"))
num2=int(input("Enter the Second number :"))
num3=''
try:
    num3=(num1/num2)
except:
    print("Enter different second value as division by ZERO is not possible ")

print(num3)