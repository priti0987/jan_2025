class vehicle:
    def __init__(self,brand,speed):
        self.brand = brand
        self.__speed = speed  #private variable

    def get_speed(self):
        return self.__speed
    def set_speed(self,new_speed):
        self.__speed = new_speed

    def show_info(self):
        print("brand = ",self.brand)
        print("speed = ",self.__speed)


class car(vehicle):
    def __init__(self,brand,speed,fuel):
        super().__init__(brand,speed)
        self.fuel = fuel
    def show_info(self):
        super().show_info()
        print("fuel = ",self.fuel)

Car1 = car("toyota",500,"petrol")
print("Initial speed = ",Car1.get_speed())
Car1.set_speed(250)
Car1.show_info()