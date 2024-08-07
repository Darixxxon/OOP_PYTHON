import Constants
import Plant

class Belladonna (Plant):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, Constants.STRENGTH_BELLADONNA, Constants.INITIATIVE_PLANT, Constants.NAME_BELLADONNA)
    
    def collision(self, orga, orgd):
        orga.setIsAlive(False)
        f"{orgd.getName()} killed {orga.getName()}"
        return 0

    def draw(self):
        return chr(Constants.DRAW_BELLADONNA)
    
    def createNew(self, x, y):
        world = self.getWorld()
        belladonna = Belladonna(world, x, y)
        world.addOrganism(belladonna)