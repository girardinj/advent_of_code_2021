from doctest import Example
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
    for irow in range(-1, len(grid)):
        for icolumn in range(len(grid[irow])):
            if irow == -1:
                if icolumn == 0:
                    print('  0', end=' ')
                else:
                    print(f'{icolumn}', end=' ')
                continue
            if icolumn == 0:
                print(f'{irow}', end=' ')
            print(grid[irow][icolumn], end=' ')
        print()
    # for row in grid:
    #     for column in row:
    #         print(column, end=' ')
    #     print()

def fold_up(grid, axis):    
    print('folding on y', axis)
    
    if len(grid) == axis * 2:
        keep_part = grid[:axis +1]
    else:
        keep_part = grid[:axis]

    folded_part = grid[axis+1:]
    
    print_grid(keep_part)
    print_grid(folded_part)
    folded_part.reverse()
    print_grid(folded_part)
    
    diff = len(keep_part[0]) - len(folded_part[0])
    for irow in range(len(folded_part)):
        for icolumn in range(len(folded_part[irow])):
            case = folded_part[irow][icolumn]
            if case == '#':
                keep_part[irow][icolumn+diff] = '#'
    
    I CAN DO ANYTHING IT DOESNT SHOW
    WHEN USING THE CHEAT IT WORKS, BUT THE CHEAT DOESNT RENDER RIGHT THE EXAMPLE
    return keep_part

def fold_left(grid, axis):
    print('folding on x', axis)
    
   
    return grid

def puzzle1(points, instructions):
    max_x = max(points, key=lambda p: p[0])[0]
    max_y = max(points, key=lambda p: p[1])[1]
    max2 = max(points, key=lambda p: p[0])

    grid = [['.' for _ in range(max_x+1)] for _ in range(max_y+1)]

    print(len(grid), len(grid[0]))
    
    for p in points:
        grid[p[1]][p[0]] = '#'
    
    for instruction in instructions:
        max_x = len(grid[0])-1
        max_y = len(grid)-1
        axis = instruction[1]
        
        print_count(grid, f'{instruction[0]} {axis}')
        # fold up
        if instruction[0] == 'y':
            grid = fold_up(grid, axis)
        # fold left
        if instruction[0] == 'x':
            grid = fold_left(grid, axis)
        # break # part 1
    
    print_count(grid, 'final')
    print_grid(grid)
    print()

    return reduce(operator.add, (1 for row in grid for column in row if column == '#'))

steps = 0
def print_count(grid, axis):
    global steps
    print('_' * 20)
    print(axis)
    print(steps, reduce(operator.add, (1 for row in grid for column in row if column == '#')))
    steps += 1

def main():
    points, instructions = get_data()
    # print(points)
    # print(instructions)
    print(puzzle1(points, instructions))

if __name__ == '__main__':
    main()
