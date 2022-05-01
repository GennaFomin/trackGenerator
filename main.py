from Element.element import Element

splitS = Element(2, 2, [2, 3], [1, 4])
x = splitS.fillGrid()
for i in range(len(x)):
    stringa = ""
    for j in range(len(x[i])):
        stringa += str(x[i][j])
    print(stringa)