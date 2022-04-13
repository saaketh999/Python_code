"""try:
    a=50
    b=int(input("Enter the value for b :"))
    print(a/b)
except ZeroDivisionError:
    print("Value of b can't be ZERO")
except ValueError:
    print("Invalid Input, !!!TRY AGAIN!!! with VALID input")"""


try:
    num1=int(input("Enter a numrator of the division :"))
    num2=int(input("Enter a denominator of the division :"))
    num3=num1/num2
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Zero can't be used as denominator")
else:
    print(num3)


