# Importing Grid module to help us manage class Element
from Grid.grid import Grid

class Element():
    """ Object of type: drone racing track elemenet """

    # class constructor
    def __init__(self, nGates, nFlags, gCord, fCord, hardness = 0):

        """ Initializing atributes of our class """
        self.nGates = nGates # number of gates in this element
        self.nFlags = nFlags # number of flags in this element
        self.gCord = gCord # Coordinates of all gates on 1 axis
        self.fCord = fCord # Coordintaes of all flags on 1 aixs

    grid = Grid()

    # method to get a matrix of elements
    def fillGrid(self):

        Element.grid.x = self.nGates
        Element.grid.y = self.nFlags

        Element.grid.coordsGates = self.gCord
        Element.grid.coordsFlags = self.fCord

        return Element.grid.getGrid()

    # temporary function, to check if optimization works properly.
    # After it will be changed with calcHardness(), which formula will be derived later and which will
    # calculate hardness based on amount of gates and flags + degrees of rotation throughout the element
    def setHardness(self, hardn):
        self.hardness = hardn

    # The next gen of setHardness()
    def calcHardness(self, degrees):
        return degrees
    # This function will be futher changes as I am still working on the formula for hardness.