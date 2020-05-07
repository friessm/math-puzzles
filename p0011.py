"""
Solution to Project Euler problem 11
https://projecteuler.net/problem=11
"""

from math import prod

def get_grid():
    grid = []
    with open('p0011.txt', 'r') as r:
        for line in r:
            grid.append([item for item in line.split()])
    return grid


def lpig(grid):  
    ''' Visit each cell, compute products and return heighest product.

    Multiplication is associative. So up, down and left, right 
    are the same. The same reduces the diagonal multiplication
    from 4 to 2.
    
    '''

    products = []
    width = len(grid[0])
    height = len(grid)
    dis = 4 # keep <4 distance from end in all directions

    for l in range(0, height):
        for n in range(0, width):
            # horizontal
            if n + dis <= width:
                products.append(prod([int(grid[l][x]) for x in range(n, n+4)]))
            
            # vertical
            if l + dis <= height:
                products.append(prod([int(grid[x][n]) for x in range(l, l+4)]))

            # top left diagonal
            if l + dis <= height and n + dis <= width:
                products.append(prod([int(grid[x][n]) for x in range(l, l+4)]))

            # bottom right diagonal
            if l + dis <= height and n - dis > -1:
                products.append(prod([int(grid[l+x][n-x]) for x in range(0, 4)]))
    return max(products)

if __name__ == '__main__':
    print(lpig(get_grid()))
    