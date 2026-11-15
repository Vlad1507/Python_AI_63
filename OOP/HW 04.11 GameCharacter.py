class GameCharacter:
    def __init__(self,name):
        self.name = name
        self.__health = 100
        self.__level = 1
    @property
    def health(self):
        return self.__health
    @property
    def level(self):
        return self.__level
    def take_damage(self,amount):
        if amount <= 0:
            raise ValueError("Урон не може бути від'ємним числом або нульовим")
        else:
            self.__health = max(0,self.__health - amount)
    def heal(self,amount):
        if amount <= 0:
            raise ValueError("Відновлення не може бути від'ємним числом або нульовим")
        else:
            self.__health = min(self.__health + amount,100)
    def level_up(self):
        self.__level += 1

hero = GameCharacter("Knight")

hero.take_damage(40)
print(hero.health)

hero.heal(20)
print(hero.health)

hero.level_up()
print(hero.level)

hero.take_damage(200)
print(hero.health)





