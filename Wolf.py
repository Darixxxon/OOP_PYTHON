import Animal
import Constants

class Wolf(Animal):
    def __init__(self, world, x, y):
        super().__init__(self, world, x, y, Constants.STRENGTH_WOLF, Constants.INITIATIVE_WOLF, Constants.NAME_WOLF)
    def draw(self):
        return chr(Constants.DRAW_WOLF)

    def createNew(self, x, y):
        world = self.getWorld()
        wolf = Wolf(world, x, y)
        world.addOrganism(wolf)