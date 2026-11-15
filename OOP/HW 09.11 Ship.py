class Ship:
    def __init__(self,name,displacement,crew):
        self.name = name
        self.displacement = displacement
        self.crew = crew

class Frigate(Ship):
    def __init__(self,name,displacement,crew,missiles):
        super().__init__(name, displacement, crew)
        self.missiles = missiles

class Destroyer(Ship):
    def __init__(self,name,displacement,crew,guns):
        super().__init__(name, displacement, crew)
        self.guns = guns

class Cruiser(Ship):
    def __init__(self,name,displacement,crew,helicopters):
        super().__init__(name, displacement, crew)
        self.helicopters = helicopters

frigate = Frigate("Storm", 4000, 200, 16)
destroyer = Destroyer("Falcon", 6000, 300, 8)
cruiser = Cruiser("Neptune", 12000, 500,4)

print(frigate.name)
print(frigate.displacement)
print(frigate.crew)
print(frigate.missiles)
print("==========")
print(destroyer.name)
print(destroyer.displacement)
print(destroyer.crew)
print(destroyer.guns)
print("=========")
print(cruiser.name)
print(cruiser.displacement)
print(cruiser.crew)
print(cruiser.helicopters)