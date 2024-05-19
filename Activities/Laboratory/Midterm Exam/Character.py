class Character:
    def __init__(self, name:str, damage:int, health:int):
        self.name = name
        self.damage = damage
        self.health = health
        self.maxHP = health
    
    def attack(self,target):
        target.health -= self.damage
        target.health = max(target.health,0)