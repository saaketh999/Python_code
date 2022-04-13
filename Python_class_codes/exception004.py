x=input("Enter the value1 :")
y=input("Enter the value2 :")
try:
    a=float(x)
    b=float(y)
    c=(a/b)
except ValueError:
    print("Check the value")
except ZeroDivisionError:
    print("Value 2 is zero")
else:
    print('No Errors!!!')