import Constants
import Plant

class Grass (Plant):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, Constants.STRENGTH_PLANT, Constants.INITIATIVE_PLANT, Constants.NAME_GRASS)
    
    def draw(self):
        return chr(Constants.DRAW_GRASS)
    
    def createNew(self, x, y):
        world = self.getWorld()
        grass = Grass(world, x, y)
        world.addOrganism(grass)