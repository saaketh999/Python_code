try:
    cash=int(input("Enter the amount to be withdrawn :"))
    if cash>1000:
        raise Exception
    else:
        print('Cash {} withdrawn'.format(cash))

except:
    print("Cash exceeds limit")

print('---------------------------------------')
try:
    cash=int(input("Enter the amount to be withdrawn :"))
    if cash>1000:
        raise Exception
    else:
        print('Cash {} withdrawn'.format(cash))

except:
    print("Cash exceeds limit")

print('--------------------------------------------')