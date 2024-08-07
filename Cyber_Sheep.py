from cmath import sqrt
import Animal
import Constants
import random

class Cyber_Sheep(Animal):
    def __init__(self, world, x, y):
        super().__init__(self, world, x, y, Constants.STRENGTH_CYBER_SHEEP, Constants.INITIATIVE_CYBER_SHEEP, Constants.NAME_CYBER_SHEEP)
    
    def action(self):
        dist = 420
        cur = 420
        for i in range(len(self.world_.organisms_)):
            if self.world_.organisms_[i].draw() == 197:
                dist1 = sqrt((self.x_-self.world_.organisms_[i].x_)**2 +(self.y_-self.world_.organisms_[i].y_)**2)
                if dist1 < dist:
                    dist = dist1
                    cur = i
        if dist == 420 and cur == 420:
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
        else:
            newX = self.x_
            newY = self.y_
            deltaX=self.x_-self.world_.organisms_[i].x_
            deltaY=self.y_-self.world_.organisms_[i].y_
            if abs(deltaX)>abs(deltaY):
                if deltaX > 0:
                    newX -=1
                else:
                    newX +=1
            else:
                if deltaY > 0:
                    newY -=1
                else:
                    newY +=1
                
            if (newX >= 0 and newX < self.world_.getTilesX() and newY >= 0 and newY < self.world_.getTilesY()):
                org = self.world_.getOrganism(newX, newY)
                if org is None:
                    self.x_ = newX
                    self.y_ = newY
                else:
                    if org.collision(self, org) == 1:
                        self.x_ = newX
                        self.y_ = newY
                
    
    def draw(self):
        return chr(Constants.DRAW_CYBER_SHEEP)

    def createNew(self, x, y):
        world = self.getWorld()
        cyber_sheep = Cyber_Sheep(world, x, y)
        world.addOrganism(cyber_sheep)