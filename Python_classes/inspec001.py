class employee:
    def getdata(self,empid,empname,salary):
        self.empid=empid
        self.empname=empname
        self.salary=salary
    def empdata(self):
        print("Employee id:",self.empid,";Employee Name :",self.empname,";Employee CTC :",self.salary)

obj=employee()
obj.getdata("1001","Dev","200000")
obj.empdata()
obj.getdata("1002","Sam","300000")
obj.empdata()
obj.getdata("1003","Anna","400000")
obj.empdata()
obj.getdata("1004","Ben","450000")
obj.empdata()