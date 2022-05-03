from Element.element import Element

# It seems like generate will become a class for:
# a) generating the set of elems
# b) generating the track

class Generate():

    def __int__(self, elemList = []):
        self.elemList = elemList

    finalElements = []

    # def optimizeElements(self, targetHardn):
        # Что если просто набивать сложными элементами пока не достигнем поставленной сложности,
        # а потом, будем добивать просто воротами, и просто флагами, сложность которых равна мнимой 1
        # И так получится, что мы сможем использовать максимум элементов + получить нужную сложность )