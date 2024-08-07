from abc import ABC, abstractmethod

class Organism(ABC):
    def __init__(self, world, x, y, strength, initiative, name, type):
        Organism.world_ = world
        self.x_ = x
        self.y_ = y
        self.strength_ = strength
        self.initiative_ = initiative
        self.age_ = 0
        self.isAlive_ = True
        self.name_ = name
        self.type_ = type
        self.abilityCD_ = 0
        self.abilityDUR_ = 0
    
    def getX(self):
        return self.x_
    def getY(self):
        return self.y_
    def getStrength(self):
        return self.strength_
    def getInitiative(self):
        return self.initiative_
    def getAge(self):
        return self.age_
    def getWorld(self):
        return self.world_
    def getCD(self):
        return self.abilityCD_
    def getDUR(self):
        return self.abilityDUR_
    def getWorld(self):
        return self.name_
    def getCD(self):
        return self.type_
    def getDUR(self):
        return self.isAlive_
    
    def setX(self, x):
        self.x_ = x
    def setY(self, y):
        self.y_ = y
    def setStrength(self, strength):
        self.strength_ = strength
    def setInitiative(self, initiative):
        self.initiative_ = initiative
    def setAge(self, age):
        self.age_ = age
    def setWorld(self, world):
        self.world_ = world
    def setCD(self, abilityCD):
        self.abilityCD_ = abilityCD
    def setDUR(self, abilityDUR):
        self.abilityDUR_ = abilityDUR
    def setIsAlive(self, isAlive):
        self.isAlive_ = isAlive
    
    @abstractmethod
    def action():
        pass
    @abstractmethod
    def collision(orga, orgd):
        pass
    @abstractmethod
    def draw():
        pass
    @abstractmethod
    def createNew(x, y):
        pass