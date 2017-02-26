"""
You are given a map in form of a two-dimensional integer grid where 1 represents
land and 0 represents water.
Grid cells are only connected horizontally and vertically.
The grid is completely surrounded by water, and there is exaclty one island

Determine the perimeter of the island.
"""
import operator


def islandPerimeter(grid):
    return sum(sum(map(operator.ne, [0] + row, row + [0]))
               for row in grid + list(map(list, zip(*grid))))


if __name__ == '__main__':
    print(islandPerimeter([[0, 1, 0, 0],
                           [1, 1, 1, 0],
                           [0, 1, 0, 0],
                           [1, 1, 0, 0]]))
