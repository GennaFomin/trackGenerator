from Grid.grid import Grid

x = Grid(10, 2, [1, 2, 3], [4, 5, 6])
yx = x.getGrid()

for i in range(len(yx)):
    for j in range(len(yx[i])):
        print(yx[i][j])
    print('')