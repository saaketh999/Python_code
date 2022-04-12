class employee:
    def details(self,name,title,year,location):
        print('name:{}\ntitle:{}\nyear of joining:{}\ncurrent location:{}'.format(name,title,year,location))

obj=employee()
obj.details('Saketh','Developer','2018','Bengaluru')
print(" ------- ---------")
obj.details('Veer','Operation','2017','Chennai')
print('-----------------')
obj.details('Dev','Tester','2020','Hyderabad')