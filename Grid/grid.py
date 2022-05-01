class Grid():

    """ Grid class will help us manage the route through the drone track element, assigning the in and out gates, and
                            all the gates that should be passed with respect to the order and level"""

    # The grid will be represented as a 2d array, where we will have a 1 if we have a gate or flag on the
    # tile and 0 if it is blank.

    # Must say that this class is all at all technical and only supports Element class

    def __init__(self, x, y, coordsGates, coordsFlags):
        self.x = x # number of gates
        self.y = y # number of flags
        self.coordsGates = coordsGates # 1d array representing gates places in the element
        self.coordsFlags = coordsFlags # 1d array representing flags places in the element

    # grid = [[0 for x in range(x + y + 2)] for y in range(2)]

    # Important note: Gates take 1 tile each, flags are 2 tiles high and 1 tile in width
    # Element will be maximum 2 tiles high and x + y + 2 tiles wide

    def getGrid(self):
        grid = [[0 for x in range(self.x + self.y + 2)] for y in range(2)]
    #     for(i in )
        return grid



