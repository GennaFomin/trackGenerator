from Element.element import Element
from Grid.grid import Grid

def test1():
    splitS = Element(2, 2, [2, 3], [1, 4])
    x = splitS.fillGrid()
    s = []
    for i in range(len(x)):
        stringa = ""
        for j in range(len(x[i])):
            stringa += str(x[i][j])
        s.append(stringa)
    assert s[0] == "010010", "Problem generating upper (or both) rows of grid of elem"
    assert s[1] == "011110", "Problem generating lower (or both) rows of grid of elem"

def run():
    test1()

run();