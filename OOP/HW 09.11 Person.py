class Brain:
    def think(self):
        print("Мозок думає")

class Heart:
    def beat(self):
        print("Серце б'ється")

class Legs:
    def walk(self):
        print("Ноги йдуть")

class Person(Brain,Heart,Legs):
    pass
person = Person()
person.think()
person.beat()
person.walk()



