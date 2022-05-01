from Element.element import Element

# We are going to have a base of elements of class "Element" and each of them will have its hardness level, so we will

# It is a function f(x, y) = hardness of track.
# It will look like dis: f(nGates, nFlags) = Summ of elements from 0 to I(HardnessOfElementNormalized^i * number of
# elements in the track layout)

# It seems like generate will become a class for:
# a) generating the set of elems
# b) generating the track

class Generate():

    def __int__(self, elemList = []):
        self.elemList = elemList

    finalElements = []

    # def optimizeElements(self, targetHardn):