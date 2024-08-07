import Animal
import Constants

class Human (Animal):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, Constants.STRENGTH_HUMAN, Constants.INITIATIVE_HUMAN, Constants.NAME_HUMAN)
    
    def action(self):
        if self.abilityCD_ > 0:
            if self.abilityDUR_ > 0:
                self.setStrength(self.getStrength()-1)
                self.abilityDUR_ = self.abilityDUR_ -1
            self.abilityCD_ = self.abilityCD_ -1
        
        newX = self.x_
        newY = self.y_
        match self.world_.getHumanMove():
            case 0:
                newX +=1
            case 1:
                newY +=1
            case 2:
                newX -=1
            case 3:
                newY -=1
        
        if newX >= 0 and newX < self. world_.getTilesX() and newX >= 0 and newY < self.world_.getTilesY():
            org = self.world_.getOrganism(newX, newY)
            if org == None:
                self.x_ = newX
                self.y_ = newY
            elif org.collision(self, org) == 1:
                self.x_ = newX
                self.y_ = newY
    
    def draw(self):
        if self.abilityDUR_>0:
            return chr(Constants.DRAW_SUPER_HUMAN)
        else:
            return chr(Constants.DRAW_NORMAL_HUMAN)
    
    def ability(self):
        #magical potion#
        if self.abilityCD_==0:
            self.setStrength(Constants.ABILITY_SET_STRENGTH)
            self.abilityCD_ = Constants.ABILITY_COOLDOWN
            self.abilityDUR_ = Constants.ABILITY_DURATION
            
    def createNew (self, newX, newY):
        pass