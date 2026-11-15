# завдання 1
class Car:
    total_cars = 0
    def __init__(self,brand,model,mileage):
        self.brand = brand
        self.model = model
        self.__mileage = mileage
        Car.total_cars += 1
    def show_info(self):
        print(self.brand)
        print(self.model)
        print(self.__mileage)
    def drive(self,km):
        self.__mileage += km
    @property
    def mileage(self):
        return self.__mileage
    @staticmethod
    def validate_mileage(km):
        if km > 0:
            return True
        else:
            return False
    @classmethod
    def show_total_cars(cls):
        print(cls.total_cars)
    # завдання 3
    @classmethod
    def from_string(cls, text):
        brand, model, mileage = text.split(",")
        return cls(brand, model, int(mileage))
# завдання 2
class ElectricCar(Car):
    def __init__(self,brand,model,mileage,battery):
        super().__init__(brand, model, mileage)
        self.battery = battery
    def charge(self,amount):
        self.battery = min(self.battery + amount,100)
    def show_info(self):
        super().show_info()
        print(self.battery)


car1 = Car("BMW", "X5", 1000)
car2 = Car("AUDI", "A6", 2500)

car1.show_info()

print("============")
car2.show_info()

print("============")

car1.drive(150)
car1.show_info()
print("============")

print(car1.validate_mileage(150))
print(car1.validate_mileage(-100))
print("============")

Car.show_total_cars()

print("============")

car3 = ElectricCar("Tesla", "Model 3", 15000, 60)
car3.show_info()

print("============")

car3.charge(30)
car3.show_info()

print("============")

car3.charge(50)
car3.show_info()
print("============")

car4 = Car.from_string("BMW,320,50000")
car4.show_info()

print("Всего автомобилей:", Car.total_cars)
