
class Grid:
    def __init__(self):
        self.grid = []
        self.column_count = 0

    def add(self, row, column, value=1):
        self.create_cells(row, column)
        self.grid[row][column] += value

    def create_cells(self, row, column):
        row_diff = row+1 - len(self.grid)
        if row_diff >= 0:
            self.grid = self.grid + [[] for _ in range(row_diff)]

        for i in range(len(self.grid)):
            column_diff = column+1 - len(self.grid[i])
            if column_diff >= 0:
                self.grid[i] = self.grid[i] + [0 for _ in range(column_diff)]

    def get_total_dangerous(self):
        tot = 0
        for row in self.grid:
            for cell in row:
                if cell >= 2:
                    tot += 1
        return tot

    def __str__(self) -> str:
        s = ''
        for row in self.grid:
            for cell in row:
                if cell == 0:
                    cell = '.'
                s += f'{cell} '
            s = s[:-1]
            s += '\n'
        s = s[:-1]
        return s
s = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''

s2 = '''1,1 -> 8,8
7,5 -> 5,3
7,5 -> 4,3
0,4 -> 8,4
0,5 -> 8,5
3,1 -> 3,6'''

s3 = '''4,4 -> 0,0
0,0 -> 0,3
3,0 -> 0,3
4,4 -> 5,5
10,10 -> 5,5
0,3 -> 3,5
8,0 -> 1,0'''

def is_diagonal(p1, p2):
    diff_x = abs(p1[0] - p2[0])
    diff_y = abs(p1[1] - p2[1])
    
    return diff_x == diff_y


def get_direction(p1, p2):
    # (5, 5) -> (3, 3)
    if p1[0] > p2[0] and p1[1] > p2[0]:
        return 'tl-br'
    # (3, 3) -> (5, 5)
    if p1[0] < p2[0] and p1[1] < p2[1]:
        return 'tl-br'
    
    return 'tr-bl'

    

def puzzle1():

    grid = Grid()
    line_counter = 0
    
    with open('day5_data.txt', 'r') as f:
        s = f.readlines()
    import re
    reg = r'(\d+),(\d+) -> (\d+),(\d+)'
    for line in s:
        line_counter += 1
        values = re.findall(reg, line)
        p1 = (int(values[0][0]), int(values[0][1]))
        p2 = (int(values[0][2]), int(values[0][3]))
        
        # print(p1, p2)

        diff_x = abs(p1[0]-p2[0])
        diff_y = abs(p1[1]-p2[1])
        x = min(p1[0], p2[0])
        y = min(p1[1], p2[1])
        
        if p1 == p2:
            print(p1, p2)
        if diff_x == 0:
            # print(p1, p2)
            for i in range(diff_y+1):
                # print(f'I add to {p1[0]}, {y+i}')
                grid.add(y+i, p1[0])

        if diff_y == 0:
            # print(p1, p2)
            for i in range(diff_x+1):
                # print(f'I add to {x+i}, {p1[1]}')
                grid.add(p1[1], x+i)
    
        if is_diagonal(p1, p2):
            if diff_x != diff_y:
                print('wtf1')
            direction = get_direction(p1, p2)
            if direction == 'tl-br':
                # print('tl-br', p1, p2)
                for i in range(diff_x+1):
                    # print(f'I add to {x+i}, {y+i}')
                    grid.add(y+i, x+i)
            elif direction == 'tr-bl':
                # print('tr-bl', p1, p2)
                for i in range(diff_x+1):
                    j = max(p1[0], p2[0]) -i
                    # print(f'I add to {j}, {y+i}')
                    grid.add(y+i, j)
            else:
                print('error direction')
                print(direction, p1, p2)
                break
    print('nb lines:', line_counter)
    # print(grid)
    with open('output.txt', 'w') as f:
        f.write(str(grid))
    # print(p1, p2)
    return grid.get_total_dangerous()

def get_pix(i):
    if i == 0:
        return [0, 0, 0]
    elif i == 1:
        return [255, 0, 0]
    elif i == 2:
        return [0, 255, 0]
    elif i == 3:
        return [0, 0, 255]
    elif i == 4:
        return [255, 255, 0]
    elif i == 5:
        return [255, 0, 255]
    elif i == 6:
        return [0, 255, 255]
    else:
        return [255, 255, 255]

def to_pic():
    import cv2
    import numpy as np
    
    image = []
    with open('output.txt', 'r') as f:
        for line in f:
            image_line = []
            for c in line:
                if c == '\n' or c == ' ':
                    continue
                if c == '.':
                    c =  '0'
                i = int(c)
                pix = get_pix(i)
                image_line.append(pix)
            image.append(image_line)
    
    image = np.array(image, dtype=np.uint8)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    exit(0)


def main():
    # to_pic()
    print(puzzle1())

if __name__ == "__main__":
    main()