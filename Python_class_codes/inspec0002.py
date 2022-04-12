#Calling class itself as a function
class Employee:
    def info(self):
        name="Tom"
        dept="Design"
        print(name+" from "+dept)

class Employee2:
    def info(self):
        name = "Sam"
        dept = "Development"
        print(name + " from " + dept)

class Employee3:
    def info(self):
        name = "Dan"
        dept = "Testing"
        print(name + " from " + dept)

obj_emp=Employee()
obj_emp.info()
obj_adm=Employee2()
obj_adm.info()
obj_test=Employee3()
obj_test.info()
