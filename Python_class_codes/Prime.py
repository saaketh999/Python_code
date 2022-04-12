for n in range(2,10):
    #When the number is prime the below loop will never break
    #Prime quality is it should not be divisible by any number below it.
    for x in range(2,n):
        if n % x == 0:
            print(f"{n} equal {x} * {n//x}")
            #As soon as it gets one thing that it is divisible by it breaks.
            break
    else:
        print(f"{n} is prime")
