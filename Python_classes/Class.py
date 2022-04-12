class drone:
    def details(self,name,function,year,usage):
        print(' name: {}\n function {}\n year of commision {} \n current usage {}'.format(name,function,year,usage))

obj=drone()
obj.details('Saketh','research','2018','50%')
print(" ------- ---------")

class drone:
    def details(self,name,function):
        print(' name {}\n function {}'.format(name,function))

obj=drone()
obj.details('err','error')

print(" ------- ---------")
class drone:
    def details(self,name,function):
        print(' name {}\n function {}'.format(name,function))

obj=drone()
obj.details('Ref','Fun')