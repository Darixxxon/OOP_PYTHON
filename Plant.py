from abc import ABC, abstractmethod
import Organism
import Constants
import random

class Plant (Organism, ABC):
    def __init__(self, world, x, y, strength, initiative, name, type):
        super().__init__(world, x, y, strength, initiative, name, Constants.TYPE_PLANT)
    
    def action(self):
        random_number_in_range = random.randint(0, Constants.SPREAD_RATE)
        if random_number_in_range == 0:
            newX = self.x_
            newY = self.y_
            random_number_in_range = random.randint(0, 3)
            match random_number_in_range:
                case 0:
                    newX +=1
                case 1:
                    newY +=1
                case 2:
                    newX -=1
                case 3:
                    newY -=1
            
            if newX >= 0 and newX < self.world_getTilesX() and newY >= 0 and newY < self.world_.getTilesY():
                org = self.world_.getOrganism(newX, newY)
                if org == None:
                    self.createNew(newX, newY)
    
    def collision(self, orga, orgd):
        if orga.getStrength() >= orgd.getStrength():
            orgd.setIsAlive(False)
            f"{orga.getName()} ate {orgd.getName()}"
            return 1
        return 0
    
    @abstractmethod
    def draw():
        pass