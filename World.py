import Organism
import Constants
import random
import Antelope
import Belladonna
import Cyber_Sheep
import Fox
import Grass
import Guarana
import Human
import Sheep
import Sosnowsky
import Sow_thistle
import Turtle
import Wolf

class World():
    isHumanLive_ = 0
    
    def __init__ (self, width, height):
        self.tilesX = width
        self.tilesY = height
        self.generateWorld(height, width, self)
    
    def generateWorld(self, height, width, world):
        r = (width*height)/100
        randomX = random.randint(0, width)
        randomY = random.randint(0, height)
        human = Human(world, randomX, randomY)
        for i in range(r+1):
            for j in range(11):
                randomX = random.randint(0, width)
                randomY = random.randint(0, height)
                org = self.getOrganism(randomX, randomY)
                if org is None:
                    match j:
                        case 0:
                            antelope = Antelope(self, randomX, randomY)
                            self.addOrganism(antelope)
                        case 1:
                            belladonna = Belladonna(self, randomX, randomY)
                            self.addOrganism(belladonna)
                        case 2:
                            fox = Fox(self, randomX, randomY)
                            self.addOrganism(fox)
                        case 3:
                            cyber_sheep = Cyber_Sheep(self, randomX, randomY)
                            self.addOrganism(cyber_sheep)
                        case 4:
                            grass = Grass(self, randomX, randomY)
                            self.addOrganism(grass)
                        case 5:
                            guarana = Guarana(self, randomX, randomY)
                            self.addOrganism(guarana)
                        case 6:
                            sheep = Sheep(self, randomX, randomY)
                            self.addOrganism(sheep)
                        case 7:
                            sosnowsky = Sosnowsky(self, randomX, randomY)
                            self.addOrganism(sosnowsky)
                        case 8:
                            sow_thistle = Sow_thistle(self, randomX, randomY)
                            self.addOrganism(sow_thistle)
                        case 9:
                            turtle = Turtle(self, randomX, randomY)
                            self.addOrganism(turtle)
                        case 10:
                            wolf = Wolf(self, randomX, randomY)
                            self.addOrganism(wolf)
    
    def getOrganism(self, x, y):
        for organism in self.organisms_:
            if organism.getX() == x and organism.getY() == y:
                return organism
        return None

    def addOrganism(self, organism):
        self.organisms_.append(organism)
        organism.setWorld(self)
    
    def makeTurn(self):
        self.organisms_ = sorted(self.organisms_, key=lambda x: (x['initiative'], x['age']), reverse=True)
        for organism in self.organisms_:
            if organism.getAge() > 0 and organism.getIsAlive() == True:
                organism.action()
        for organism in self.organisms_:
            if organism.getIsAlive() == False:
                del organism
            organism.setAge(organism.getAge() + 1)
    def getTilesX(self):
        return self.tilesX
    
    def getTilesY(self):
        return self.tilesY
    
    def save(self, file):
        with open(file, 'w') as f:
            f.write(str(self.getTilesX()) + '\n')
            f.write(str(self.getTilesY()) + '\n')
            f.write(str(len(self.organisms_)) + '\n')
            for organism in self.organisms_:
                if organism is not None:
                    f.write(organism.draw() + '\n')
                    f.write(str(organism.getX()) + '\n')
                    f.write(str(organism.getY()) + '\n')
                    f.write(str(organism.getStrength()) + '\n')
                    f.write(str(organism.getInitiative()) + '\n')
                    f.write(str(organism.getAge()) + '\n')
                    f.write(str(organism.getIsAlive()) + '\n')
                    if organism.draw() == 'h' or organism.draw() == 'H':
                        f.write(str(organism.getCD()) + '\n')
                        f.write(str(organism.getDUR()) + '\n')
    
    def open(self, file):
        with open(file, 'r') as f:
            reader = f.readlines()
            tilesX = int(reader[0].strip())
            tilesY = int(reader[1].strip())
            self.tilesX = tilesX
            self.tilesY = tilesY
            self.organisms_.clear()
            num = int(reader[2].strip())
            for i in range(3, 3+num*9, 9):
                draw = reader[i].strip()
                x = int(reader[i+1].strip())
                y = int(reader[i+2].strip())
                
                if draw == Constants.DRAW_NORMAL_HUMAN or draw == Constants.DRAW_SUPER_HUMAN:
                    human = Human(self, x, y)
                    self.addOrganism(human)
                    human.setStrength(int(reader[i+3].strip()))
                    human.setInitiative(int(reader[i+4].strip()))
                    human.setAge(int(reader[i+5].strip()))
                    human.setIsAlive(bool(reader[i+6].strip()))
                    human.setCD(int(reader[i+7].strip()))
                    human.setDUR(int(reader[i+8].strip()))
                
                elif draw == Constants.DRAW_ANTELOPE:
                    antelope = Antelope(self, x, y)
                    self.addOrganism(antelope)
                    antelope.setStrength(int(reader[i+3].strip()))
                    antelope.setInitiative(int(reader[i+4].strip()))
                    antelope.setAge(int(reader[i+5].strip()))
                    antelope.setIsAlive(bool(reader[i+6].strip()))
                
                elif draw == Constants.DRAW_BELLADONNA:
                    belladonna = Belladonna(self, x, y)
                    self.addOrganism(belladonna)
                    belladonna.setStrength(int(reader[i+3].strip()))
                    belladonna.setInitiative(int(reader[i+4].strip()))
                    belladonna.setAge(int(reader[i+5].strip()))
                    belladonna.setIsAlive(bool(reader[i+6].strip()))
                    
                elif draw == Constants.DRAW_CYBER_SHEEP:
                    Cyber_sheep = Cyber_Sheep(self, x, y)
                    self.addOrganism(Cyber_sheep)
                    belladonna.setStrength(int(reader[i+3].strip()))
                    belladonna.setInitiative(int(reader[i+4].strip()))
                    belladonna.setAge(int(reader[i+5].strip()))
                    belladonna.setIsAlive(bool(reader[i+6].strip()))
                
                elif draw == Constants.DRAW_FOX:
                    fox = Fox(self, x, y)
                    self.addOrganism(fox)
                    fox.setStrength(int(reader[i+3].strip()))
                    fox.setInitiative(int(reader[i+4].strip()))
                    fox.setAge(int(reader[i+5].strip()))
                    fox.setIsAlive(bool(reader[i+6].strip()))
                
                elif draw == Constants.DRAW_SHEEP:
                    sheep = Sheep(self, x, y)
                    self.addOrganism(sheep)
                    sheep.setStrength(int(reader[i+3].strip()))
                    sheep.setInitiative(int(reader[i+4].strip()))
                    sheep.setAge(int(reader[i+5].strip()))
                    sheep.setIsAlive(bool(reader[i+6].strip()))
                
                elif draw == Constants.DRAW_GRASS:
                    grass = Grass(self, x, y)
                    self.addOrganism(grass)
                    grass.setStrength(int(reader[i+3].strip()))
                    grass.setInitiative(int(reader[i+4].strip()))
                    grass.setAge(int(reader[i+5].strip()))
                    grass.setIsAlive(bool(reader[i+6].strip()))
                
                elif draw == Constants.DRAW_GUARANA:
                    guarana = Guarana(self, x, y)
                    self.addOrganism(guarana)
                    guarana.setStrength(int(reader[i+3].strip()))
                    guarana.setInitiative(int(reader[i+4].strip()))
                    guarana.setAge(int(reader[i+5].strip()))
                    guarana.setIsAlive(bool(reader[i+6].strip()))
                
                elif draw == Constants.DRAW_SOSNOWSKY:
                    sosnowsky = Sosnowsky(self, x, y)
                    self.addOrganism(sosnowsky)
                    sosnowsky.setStrength(int(reader[i+3].strip()))
                    sosnowsky.setInitiative(int(reader[i+4].strip()))
                    sosnowsky.setAge(int(reader[i+5].strip()))
                    sosnowsky.setIsAlive(bool(reader[i+6].strip()))
                
                elif draw == Constants.DRAW_SOW_THISTLE:
                    sow_thistle = Sow_thistle(self, x, y)
                    self.addOrganism(sow_thistle)
                    sow_thistle.setStrength(int(reader[i+3].strip()))
                    sow_thistle.setInitiative(int(reader[i+4].strip()))
                    sow_thistle.setAge(int(reader[i+5].strip()))
                    sow_thistle.setIsAlive(bool(reader[i+6].strip()))
                
                elif draw == Constants.DRAW_TURTLE:
                    turtle = Turtle(self, x, y)
                    self.addOrganism(turtle)
                    turtle.setStrength(int(reader[i+3].strip()))
                    turtle.setInitiative(int(reader[i+4].strip()))
                    turtle.setAge(int(reader[i+5].strip()))
                    turtle.setIsAlive(bool(reader[i+6].strip()))
                
                elif draw == Constants.DRAW_WOLF:
                    wolf = Wolf(self, x, y)
                    self.addOrganism(wolf)
                    wolf.setStrength(int(reader[i+3].strip()))
                    wolf.setInitiative(int(reader[i+4].strip()))
                    wolf.setAge(int(reader[i+5].strip()))
                    wolf.setIsAlive(bool(reader[i+6].strip()))