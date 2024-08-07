import Animal
import Constants
import random

class Fox (Animal):
    def __init__(self, world, x, y):
        super().__init__(self, world, x, y, Constants.STRENGTH_FOX, Constants.INITIATIVE_FOX, Constants.NAME_FOX)
    
    def action(self):
        newX = self.x_
        newY = self.y_
        while True:
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
            org = self.world_.getOrganism(newX, newY)
            if org == None or org.getStrength() <= self.strength_:
                break
            if (self.world_.getOrganism(self.x_ + 1, self.y_) != None and self.world_.getOrganism(self.x_ + 1, self.y_).getStrength() > self.strength_) or self.x_ + 1 >= self.world_.getTilesX():
                if (self.world_.getOrganism(self.x_ - 1, self.y_) != None and self.world_.getOrganism(self.x_ - 1, self.y_).getStrength() > self.strength_) or self.x_ - 1 < 0:
                    if (self.world_.getOrganism(self.x_, self.y_ + 1) != None and self.world_.getOrganism(self.x_, self.y_ + 1).getStrength() > self.strength_) or self.y_ + 1 >= self.world_.getTilesY():
                        if (self.world_.getOrganism(self.x_, self.y_ - 1) != None and self.world_.getOrganism(self.x_, self.y_ - 1).getStrength() > self.strength_) or self.y_ - 1 < 0:
                            break
        if newX >= 0 and newX < self.world_.getTilesX() and newY >= 0 and newY < self. world_.getTilesY():
            org = self.world_.getOrganism(newX, newY)
            if org == None:
                self.x_ = newX
                self.y_ = newY
            else:
                if org.collision(self, org) == 1:
                    self.x_ = newX
                    self.y_ = newY
    def draw(self):
        return chr(Constants.DRAW_FOX)
    
    def createNew(self, x, y):
        world = self.getWorld()
        fox = Fox(world, x, y)
        world.addOrganism(fox)