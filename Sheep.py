import Animal
import Constants

class Sheep(Animal):
    def __init__(self, world, x, y):
        super().__init__(self, world, x, y, Constants.STRENGTH_SHEEP, Constants.INITIATIVE_SHEEP, Constants.NAME_SHEEP)
    def draw(self):
        return chr(Constants.DRAW_SHEEP)

    def createNew(self, x, y):
        world = self.getWorld()
        sheep = Sheep(world, x, y)
        world.addOrganism(sheep)