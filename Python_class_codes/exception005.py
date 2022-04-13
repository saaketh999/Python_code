try:
    age=int(input("Enter the age :"))
    if(age>=18):
        raise ValueError
    else:
        print("Age is below 18")

except ValueError:
    print("User's age is above 18 he/she is not eligible under this category")