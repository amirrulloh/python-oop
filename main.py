class Hero:
    
    #Private class variabel
    __jumlah = 0

    def __init__(self, name, healt, attPower, armor):
        self.__name = name
        self.__healthStandar = healt
        self.__attPowerStandar = attPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0 #Experience

        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1
    
    @property
    def info(self):
        return "{} Level {}:\n\t health = {}/{} \n\t attack = {} \n\t armor = {}".format(self.__name, self.__level, self.__health, self.__healthMax, self.__attPower, self.__armor)
    
    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(self.__name, 'Level Up')
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level
    
    def attack(self, musuh):
        self.gainExp = 50



haya = Hero("Hayabusa", 100, 5, 10)
siber = Hero("Siber", 100, 5, 10)
print(haya.info)
haya.attack(siber)
haya.attack(siber)
haya.attack(siber)
print(haya.info)

   