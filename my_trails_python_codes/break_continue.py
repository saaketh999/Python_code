#Code example for break
"""car = ['ok','ok','ok','faulty','ok','ok']
for status in car:
    if status=='faulty':
        print(f"Car is {status}, stopping production")
        break  # This will stop the code here
    print(f"Car is {status}")
    print("Car is shipping to wearhouse")"""


"""Code example for continue"""

#Code example for break
car = ['ok','ok','ok','faulty','ok','ok']
for status in car:
    if status=='faulty':
        print(f"Encountred {status} car, Skipping shipment and moving on !!!!")
        continue   # This will take the code to start of the loop again by skipping below code.
    print(f"Car is {status}")
    print("Car is shipping to wearhouse")