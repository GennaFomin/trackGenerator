from Element.element import Element

# Getting elements we can use for the generation
# For now we realise algo with usual istream in python, later add telegram bot to handle this stuff and output result


def getElems():
    print("Hi, please enter the nuber of gates and flags you have to build a track (minimum 3 of each is neccessary for"
          "proper work of algo)")
    gates = int(input())
    flags = int(input())
    print("Please enter the hardness level you wish to have (1 - 10)")
    hardness = int(input())
    return gates, flags, hardness


# Here we go for introducing hardness metric, which I introduce based on my own experince.
# We are going to have a base of elements of class "Element" and each of them will have its hardness level, so we will
# be just optimizing a function of two variables, where x = number of gates, y = number of flags
# f(x, y) = hardness of track

# def optimizeUsage(nGates, nFlags):


