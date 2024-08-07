import Constants
import Plant

class Sosnowsky (Plant):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, Constants.STRENGTH_SOSNOWSKY, Constants.INITIATIVE_PLANT, Constants.NAME_SOSNOWSKY)
        
    def action(self):
        nowX = self.getX()
        nowY = self.getY()
        
        org = self.world_.getOrganism(nowX+1, nowY)
        if org != None and org.getType() == 'A':
            self.collision(org, self)
        org = self.world_.getOrganism(nowX-1, nowY)
        if org != None and org.getType() == 'A':
            self.this.collision(org, self)
        org = self.world_.getOrganism(nowX, nowY+1)
        if org != None and org.getType() == 'A':
            self.this.collision(org, self)
        org = self.world_.getOrganism(nowX, nowY-1)
        if org != None and org.getType() == 'A':
            self.this.collision(org, self)
            
    def collision (self, orga, orgd):
        orga.setIsAlive(False)
        f"{orgd.getName()} killed {orga.getName()}"
        return 1
    
    def draw(self):
        return chr(Constants.DRAW_SOSNOWSKY)
    
    def createNew(self, x, y):
        pass