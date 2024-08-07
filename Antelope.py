import Animal
import Constants
import random

class Antelope (Animal):
    def __init__(self, world, x, y):
        super().__init__(self, world, x, y, Constants.STRENGTH_ANTELOPE, Constants.INITIATIVE_ANTELOPE, Constants.NAME_ANTELOPE)
    
    def action(self):
        newX = self.x_
        newY = self.y_
        random_number_in_range = random.randint(0, 3)
        match random_number_in_range:
            case 0:
                newX +=2
            case 1:
                newY +=2
            case 2:
                newX -=2
            case 3:
                newY -=2
                

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
            random_number_in_range = random.randint(0, 3)
            if random_number_in_range == 1:
                f=0
                while f!=4:
                    f=0
                    if self.world_.getOrganism(orgd.getX()+1, orgd.getY()) != None or orgd.getX() + 1 >= self.world_.getTilesX():
                        f+=1
                        if self.world_.getOrganism(orgd.getX() - 1, orgd.getY()) != None or orgd.getX() - 1 < 0:
                            f+=1
                            if self.world_.getOrganism(orgd.getX(), orgd.getY() + 1) != None or orgd.getY() + 1 >= self.world_getTilesY():
                                f+=1
                                if self.world_.getOrganism(orgd.getX(), orgd.getY() - 1) != None or orgd.getY() - 1 < 0:
                                    f += 1
                    orgX = orgd.getX()
                    orgY = orgd.getY()
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
                    org1 = self.world_.getOrganism(orgX, orgY)
                    if orgX >= 0 and orgX < self.world_.getTilesX() and orgY >= 0 and orgY < self.wolrd_.getTilesY() and org1 == None:
                        orgd.setX(orgX)
                        orgd.setY(orgY)
                        return 0
            else:
                if orga.getStrength() >= orgd.getStrength():
                    orgd.setIsAlive(False)
                    f"{orga.getName()} killed {orgd.getName()}"
                    return 1
                else:
                    return 0
        return 0
    
    def draw(self):
        return chr(Constants.DRAW_ANTELOPE)
    
    def createNew(self, x, y):
        world = self.getWorld()
        antelope = Antelope(world, x, y)
        world.addOrganism(antelope)