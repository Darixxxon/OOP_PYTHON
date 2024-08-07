import Constants
import Plant
import random

class Sow_thistle (Plant):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, Constants.STRENGTH_PLANT, Constants.INITIATIVE_PLANT, Constants.NAME_SOW_THISTLE)
    
    def action (self):
        for i in range(3):
            random_number_in_range = random.randint(0,3)
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
    
    def draw(self):
        return chr(Constants.DRAW_SOW_THISTLE)
    
    def createNew(self, x, y):
        world = self.getWorld()
        sow_thistle = Sow_thistle(world, x, y)
        world.addOrganism(sow_thistle)