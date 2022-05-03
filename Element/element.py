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

    # Implement dictionary of routes and their degrees
    # A rout is a list where each even element is x - cord of tile in Grid, while each odd is y - cord of tile in Grid

    routes = {}

    # addRoute function will be a part of getElements function implimented later on
    # First we caluclate angle of rotation inside the element;
    def addRoute(self, route):
        angle = 0
        if(len(route) == 2):
            Element.routes[repr(route)] = angle
            return
        angle = (len(route) * 90) / 2
        Element.routes[repr(route)] = angle
        return

    def fillGrid(self):

        Element.grid.x = self.nGates
        Element.grid.y = self.nFlags

        Element.grid.coordsGates = self.gCord
        Element.grid.coordsFlags = self.fCord

        return Element.grid.getGrid()
    # method to get a matrix of elements

    # temporary function, to check if optimization works properly.
    # After it will be changed with calcHardness(), which formula will be derived later and which will
    # calculate hardness based on amount of gates and flags + degrees of rotation throughout the element
    def setHardness(self, hardn):
        self.hardness = hardn

    # Here we need to fill route as a repr([x1, y1, ......., xn, yn]
    # For now i decided to use some easy way to calc hardness, I found out that pretty much for all the hard elements,
    # you get 540 degrees of turn, so we will normalize degrees by dividing on 540 and i think it is fine if some elem
    # Will have more that 540, it will mean that it is HARD
    # I will need to fine tune the formula later on, maybe add some multiplicative coefficient or change the divisor
    # add different weight to gates and flags ( actually rather good idea )
    def calcHardness(self, route):
        return Element.routes[route] / 540

    # This function will be futher changes as I am still working on the formula for hardness.