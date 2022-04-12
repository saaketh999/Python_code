class rectangle:
    def __init__(self,length,breadth):
        self.l = length
        self.b = breadth
    def area(self):
        return self.l*self.b

class square:
    def __init__(self,side):
        self.s = side

    def area(self):
        return self.s ** 2
#length=float(input("Enter the length of rectangle :"))
#breadth=float(input("Enter the Breadth of rectangle :"))
#side=float(input("Enter length of the side of the square :"))
print("******************")
rect=rectangle(20,45)
print("Area of rectangle is :", rect.area())
print("*******************")
squ=square(30)
print("Area of square is : ", squ.area())

#New structure below which is areplica of above structure for future programming like API's

class rectangle:
    def __init__(self,length,breadth):
        self.l = length
        self.b = breadth
    def area(self):
        return self.l*self.b

class square:
    def __init__(self,side):
        self.s = side

    def area(self):
        return self.s ** 2


print("******************")
rect=rectangle(20,40)
print("Area of rectangle is :", rect.area())
print("*******************")
squ=square(30)
print("Area of square is : ", squ.area())
