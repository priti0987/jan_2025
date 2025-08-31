class first:
    def sing(self):
        print("User is singer")

a =first()
a.sing()


#Encapsulation

class comp:
    def __init__(self):
        self.__maxPrice = 900

    def sell(self):
        print(" price  ",self.__maxPrice)

    def setMaxPrice(self,price):
        self.__maxPrice=price


c=comp()
c.sell()

#you cant change private value
c.__maxPrice  = 1000
c.sell()

c.setMaxPrice(1500)
c.sell()