import Constants
import Plant

class Guarana (Plant):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, Constants.STRENGTH_PLANT, Constants.INITIATIVE_PLANT, Constants.NAME_GURANA)
        
    def collision(self, orga, orgd):
        if orga.getStrength() >= orgd.getStrength():
            orgd.setIsAlive(False)
            orga.setStrength(orga.getStrength() + 3)
            f"{orga.getName()} ate {orgd.getName()}"
            return 1
        return 0
    
    def draw(self):
        return chr(Constants.DRAW_GUARANA)
    
    def createNew(self, x, y):
        world = self.getWorld()
        guarana = Guarana(world, x, y)
        world.addOrganism(guarana)