"""This below code is to check the distiction between 'is' and '==' operators """
"""a=[1,2,3,4,5]
#b=[1,2,3,4,5]
b=a
print(a==b)
print(a is b)
print(id(a))
print(id(b))"""

""" Same as above for diffrent varients"""

"""numb=[1,2,3,4]
new_numb=numb + [5]
numb.append(5)
print(f"{new_numb},{numb}")
print(new_numb==numb)
print(new_numb is numb)
print(f"{id(new_numb)},{id(new_numb)}")"""

""" Task 3: Whether a number is positive , negative or Zero """

"""a = float(input("Enter the value you want to determain the status of: "))
if a < 0:
    print("Entered number is negative")
elif a > 0:
    print("Entered number is Positive")
else:
    print("You have entered zero") """

"""Employee overtime program"""

hours_worked = float(input("Enter number of hours you worked this week : "))
hourly_wage = float(input("Enter your hourly wage as per your contract: "))


if hours_worked > 40:
    overtime = (hours_worked - 40)
    overtime_wage = ((0.1 * hourly_wage) + (hourly_wage)) * overtime
    actual_wage = (40 * hourly_wage)
    print(f"You're eligible for overtime for {overtime} hours, which amounts to {overtime_wage}")
    print(f"Total amount you receive is {(overtime_wage)+(actual_wage)}")
else:
    print(f"You are not eligible for overtime as you only worked for {hours_worked}")
    print(f"You will only receive {(hours_worked)*(hourly_wage)} dollars")
