class vehicle:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
    def show_info(self):
        print("brand = ",self.brand)
        print("speed = ",self.speed)

class car(vehicle):
    def __init__(self,brand,speed,fuel):
        super().__init__(brand,speed)
        self.fuel = fuel
    def show_info(self):
        super().show_info()
        print("fuel = ",self.fuel)

Vehicle = vehicle("maruti",600)
Car = car("toyota",500,"petrol")

Vehicle.show_info()
Car.show_info()