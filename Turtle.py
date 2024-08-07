import Animal
import Constants
import random

class Turtle (Animal):
    def __init__(self, world, x, y):
        super().__init__(self, world, x, y, Constants.STRENGTH_TURTLE, Constants.INITIATIVE_TURTLE, Constants.NAME_TURTLE)
    
    def action (self):
        random_number_in_range = random.randint(0, 3)
        if random_number_in_range==3:
            random_number_in_range = random.randint(0, 3)
            newX = self.x_
            newY = self.y_
            match random_number_in_range:
                case 0:
                    newX +=1
                case 1:
                    newY +=1
                case 2:
                    newX -=1
                case 3:
                    newY -=1
        
        if newX >= 0 and newX < self.world_getTilesX() and newY > 0 and newY < self.world_.getTilesY():
            org = self.world_.getOrganism(newX, newY)
            if org == None:
                self.x_ = newX
                self.y_ = newY
            elif org.collision(self, org) == 1:
                self.x_ = newX
                self.y_ = newY
    
    def collision (self, orga, orgd):
        if orga.getName()==orgd.getName():
            self.detectFree(self.getX(), self.getY())
        elif orga.getStrength() < 5:
            return 0
        elif orga.getStrength() >= orgd.getStrength():
            orgd.setIsAlive(False)
            f"{orga.getName()} killed {orgd.getName()}"
            return 1
        return 0
    
    def draw(self):
        return chr(Constants.DRAW_TURTLE)
    
    def createNew(self, x, y):
        world = self.getWorld()
        turtle = Turtle(world, x, y)
        world.addOrganism(turtle)