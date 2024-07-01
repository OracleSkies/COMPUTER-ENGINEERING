class Character:
    def __init__(self, name:str, damage:int, health:int):
        self.name = name
        self.damage = damage
        self.health = health
        self.maxHP = health

    def attack(self, target):
        target.health -= self.damage
        target.health = max(target.health,0)

class Wizard(Character):
    def __init__(self,name:str, damage:int, health:int, mana: int, power:int):
        super().__init__(name,damage,health)
        self.mana = mana
        self.__power = power
    
    def getPower(self):
        return self.__power
    
    def setPower(self, power):
        self.__power = power
    
    def fireball(self,target):
        super().attack(target)