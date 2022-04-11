import re
from functools import reduce
import operator

def get_data():
    s = '''
        6,10
        0,14
        9,10
        0,3
        10,4
        4,11
        6,0
        6,12
        4,1
        0,13
        10,12
        3,4
        3,0
        8,4
        1,10
        2,14
        8,10
        9,0

        fold along y=7
        fold along x=5
    '''
    with open('day13_data.txt') as f:
        s = f.read()

    points = []
    instructions = []
    before_fold = True
    for line in s.strip().splitlines():
        line = line.strip()
        if line == '':
            before_fold = False
            continue
        if before_fold:
            x, y = line.split(',')
            x, y = int(x), int(y)
            points.append((x, y))
        else:
            matches = re.match(r'^fold along (x|y)=(\d+)$', line)
            instructions.append((matches.group(1), int(matches.group(2))))
            

    return points, instructions


def print_grid(grid):
    for row in grid:
        for column in row:
            print(column, end=' ')
        print()


def puzzle1(points, instructions):
    max_x = max(points, key=lambda p: p[0])[0]
    max_y = max(points, key=lambda p: p[1])[1]
    max2 = max(points, key=lambda p: p[0])

    grid = [['.' for _ in range(max_x+1)] for _ in range(max_y+1)]


    for p in points:
        grid[p[1]][p[0]] = '#'
    
    # print_grid(grid)
    # print()
    for instruction in instructions:
        max_x = len(grid[0])-1
        max_y = len(grid)-1
        axis = instruction[1]
        
        # fold up
        if instruction[0] == 'y':
            for y in range(axis):
                y_mirror = max_y - y
                for x in range(max_x+1):
                    if grid[y_mirror][x] == '#':
                        grid[y][x] = '#'
                del grid[y_mirror]
            if (max_y + 1) % 2 != 0: # if folding on a line, and not between two
                del grid[axis]

        # fold left
        if instruction[0] == 'x':
            for y in range(max_y+1):
                for x in range(axis):
                    x_mirror = max_x - x
                    if grid[y][x_mirror] == '#':
                        grid[y][x] = '#'
                    del grid[y][x_mirror]
                if (max_x + 1) % 2 != 0: # if folding on a line, and not between two
                    del grid[y][axis]
    
    print(len(grid[0]))
    # print_grid(grid)
    print()

    return reduce(operator.add, (1 for row in grid for column in row if column == '.'))

def main():
    points, instructions = get_data()
    # print(points)
    # print(instructions)
    print(puzzle1(points, instructions))

if __name__ == '__main__':
    main()
