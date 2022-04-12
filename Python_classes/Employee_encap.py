class employee:
    def __init__(self,empid,empname,salary,designation,yoj):

        self.empid=empid
        self.empname=empname
        self.salary = salary
        self.designation = designation
        self.yoj= yoj

emp1 = employee(1001,"Saketh",450000,'Operations',2017)

print("Employee details")
print("*******************************")

print("Employee ID :",emp1.empid)
print("Employee name:",emp1.empname)
print("Salary :",emp1.salary)
print("Designation :",emp1.designation)
print("Year of Joining:",emp1.yoj)