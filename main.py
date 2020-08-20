class Hero:
    
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

    #void
    def siapa(self):
        print(f"namaku {self.name}")
    
    #argumen
    def healthUp(self, up):
        self.health += up
    
    #return
    def getHealth(self):
        return self.health

hero1 = Hero("Snipper", 100, 10, 5)
hero2 = Hero("Mirana", 90, 5 ,6)


hero1.siapa()
hero1.healthUp(10)

print(hero1.getHealth())
