class Device:
    def __init__(self,brand,model,power):
        self.brand = brand
        self.model = model
        self.power = power

class CoffeeMachine(Device):
    def __init__(self,brand,model,power,water_tank):
        super().__init__(brand, model, power)
        self.water_tank = water_tank
    def make_coffee(self):
        print(f"Каву готує кавомашина {self.brand}")

class Blender(Device):
    def __init__(self,brand,model,power,speed_modes):
        super().__init__(brand, model, power)
        self.speed_modes = speed_modes
    def blend(self):
        print(f"Блендер {self.brand} подрібнює продукти!")

class MeatGrinder(Device):
    def __init__(self,brand,model,power,grinding_capacity):
        super().__init__(brand, model, power)
        self.grinding_capacity = grinding_capacity
    def grind_meat(self):
        print(f"М'ясорубка {self.brand} перемелює м'ясо!")

device = Device("Samsung", "Smart-100", 1500)
print(device.brand)
print(device.model)
print(device.power)
print("============")
coffe_machine = CoffeeMachine("Philips", "EP2220", 1500, 1.8)
print(coffe_machine.brand)
print(coffe_machine.model)
print(coffe_machine.power)
print(coffe_machine.water_tank)
coffe_machine.make_coffee()
print("============")
blender = Blender("Philips", "AH23500", 3500, 5)
print(blender.brand)
print(blender.model)
print(blender.power)
print(blender.speed_modes)
blender.blend()
print("============")
grind = MeatGrinder("Bosch", "VV4455", 4000, 3)
print(grind.brand)
print(grind.model)
print(grind.power)
print(grind.grinding_capacity)
grind.grind_meat()
