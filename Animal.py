from abc import ABC, abstractmethod
import Organism
import Constants
import random
import World

class Animal (Organism, ABC):
    def __init__(self, world, x, y, strength, initiative, name):
        super().__init__(world, x, y, strength, initiative, name, Constants.TYPE_ANIMAL)
        
    def action(self):
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

        if (newX >= 0 and newX < self.world_.getTilesX() and newY >= 0 and newY < self.world_.getTilesY()):
            org = self.world_.getOrganism(newX, newY)
            if org is None:
                self.x_ = newX
                self.y_ = newY
            else:
                if org.collision(self, org) == 1:
                    self.x_ = newX
                    self.y_ = newY
                    
    def collision(self, orga, orgd):
        if orga.getName() == orgd.getName():
            self.detectFree(self.getX(), self.getY())
        else:
            if orga.getStrength() >= orgd.getStrength():
                orgd.setIsAlive(False)
                f"{orga.getName()} killed {orgd.getName()}"
                return 1
        return 0
    @abstractmethod
    def draw():
        pass
    @abstractmethod
    def createNew(x, y):
        pass
    def detectFree(self, x, y):
        while True:
            if self.world_.getOrganism(x+1, y) != None or x + 1 >= self.world_.getTilesX():
                if self.world_.getOrganism(x-1, y) != None or x - 1 < 0:
                    if self.world_.getOrganism(x, y+1) != None or y + 1 >= self.world_.getTilesY():
                        if self.world_.getOrganism(x, y-1) != None or y - 1 < 0:
                            break
        newX = x
        newY = y
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
        world_ = self.getWorld()
        if newX >= 0 and newX < world_.getTilesX() and newY >= 0 and newY < world_.getTilesY():
            org = world_.getOrganism(newX, newY)
            if(org is None):
                self.createNew(newX, newY)
                return