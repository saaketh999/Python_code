class bike:
    def __init__(self,price,speed,milage,color,yom):

        self.price=price
        self.speed=speed
        self.milage = milage
        self.color = color
        self.yom= yom

honda = bike(150000,180,45,'black',2018)
dio = bike(200000,200,52,'blue',2017)
pulsar = bike(250000,190,34,'silver',2020)
vespa = bike(90000,80,35,'Yellow',2019)
bmw = bike(1000000,160,30,'Cyan',2022)

print("*******************************")
print("Honda bike description")
print("Price of the bike:",honda.price)
print("Top speed",honda.speed)
print("Milage",honda.milage)
print("Color of the bike :",honda.color)
print("Year of manufacture:",honda.yom)

print("*******************************")
print("Dio bike description")
print("Price of the bike:",dio.price)
print("Top speed",dio.speed)
print("Milage",dio.milage)
print("Color of the bike :",dio.color)
print("Year of manufacture:",dio.yom)


print("*******************************")
print("Pulsar bike description")
print("Price of the bike:",pulsar.price)
print("Top speed",pulsar.speed)
print("Milage",pulsar.milage)
print("Color of the bike :",pulsar.color)
print("Year of manufacture:",pulsar.yom)

print("*******************************")
print("Vespa bike description")
print("Price of the bike:",vespa.price)
print("Top speed",vespa.speed)
print("Milage",vespa.milage)
print("Color of the bike :",vespa.color)
print("Year of manufacture:",vespa.yom)

print("*******************************")
print("BMW bike description")
print("Price of the bike:",bmw.price)
print("Top speed",bmw.speed)
print("Milage",bmw.milage)
print("Color of the bike :",bmw.color)
print("Year of manufacture:",bmw.yom)




###Add more parameters to the bike fuction