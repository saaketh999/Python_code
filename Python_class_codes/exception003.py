x=input("enter the value")
y=input("enter the value")
try:
    a=int(x)
    b=int(y)
    c=a/b
except ZeroDivisionError:
    print("check the value2")


