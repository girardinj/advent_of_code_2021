
import operator
from functools import reduce
from termcolor import colored
import colorama

# need to init colorama for git bash
colorama.init()

def get_data():
    s = '''
    2199943210
    3987894921
    9856789892
    8767896789
    9899965678
    '''
    with open('day9_data.txt', 'r') as f:
        s = f.read()
    
    ret = []
    for line in s.strip().splitlines():
        row = []
        for num in line.strip():
            row.append(int(num))
        ret.append(row)
    
    return ret

def puzzle1(data):
    lowest_location = []
    
    n_rows = len(data)
    n_columns = len(data[0])
    for row in data:
        assert len(row) == n_columns, 'row length mismatch, data is not rectangular'
    
    get_top = lambda i, j : data[i - 1][j]
    get_left = lambda i, j: data[i][j - 1]
    get_right = lambda i, j: data[i][j + 1]
    get_bot = lambda i, j: data[i + 1][j]

    for row_index in range(n_rows):
        for column_index in range(n_columns):
            actual = data[row_index][column_index]
            positions = []
            
            # got something left
            if column_index > 0:
                positions.append(get_left(row_index, column_index))
            # got something right
            if column_index < n_columns - 1:
                positions.append(get_right(row_index, column_index))
            # got something top
            if row_index > 0:
                positions.append(get_top(row_index, column_index))
            # got something bot
            if row_index < n_rows - 1:
                positions.append(get_bot(row_index, column_index))
            
            
            if len(positions) > 0 and actual < min(positions):
                lowest_location.append(actual)
            
    return reduce(operator.add, lowest_location, len(lowest_location))

class Bassin():
    def __init__(self, data, center) -> None:
        self.data = data
        self.center = center
        self.bassin = [center]
        self.external_points = [center]
        self.grow()

    def __str__(self) -> str:
        return f'Bassin({self.center})'

    def debug(self) -> None:
        print(self)
        for row in range(len(self.data)):
            for col in range(len(self.data[row])):
                p = (row, col)
                if p == self.center:
                    print('\033[91m' + str(self.data[row][col]) + '\033[0m', end='')
                elif p in self.bassin:
                    print('\033[94m' + str(self.data[row][col]) + '\033[0m', end='')
                else:
                    print(self.data[row][col], end='')
            print('')

    def f(self, point, actual_value, new_external_points):
        point_value = self.data[point[0]][point[1]]
        if point_value < 9 and point_value > actual_value and point not in self.bassin:
            new_external_points.append(point)
            self.bassin.append(point)

    def grow(self):
        should_continue = True
        while should_continue:
            should_continue = False
            new_external_points = []
            for external_point in self.external_points:
                row, col = external_point
                actual_value = self.data[row][col]
                # can go left
                if row > 0:
                    point = (row - 1, col)
                    self.f(point, actual_value, new_external_points)
                # can go right
                if row < len(self.data) - 1:
                    point = (row + 1, col)
                    self.f(point, actual_value, new_external_points)
                # can go top
                if col > 0:
                    point = (row, col - 1)
                    self.f(point, actual_value, new_external_points)
                # can go bot
                if col < len(self.data[0]) - 1:
                    point = (row, col + 1)
                    self.f(point, actual_value, new_external_points)
            
            self.external_points = new_external_points
            should_continue = len(self.external_points) > 0
    
    def __len__(self):
        return len(self.bassin) 

def puzzle2(data):
    n_rows = len(data)
    n_columns = len(data[0])
    for row in data:
        assert len(row) == n_columns, 'row length mismatch, data is not rectangular'
    
    get_top = lambda i, j : data[i - 1][j]
    get_left = lambda i, j: data[i][j - 1]
    get_right = lambda i, j: data[i][j + 1]
    get_bot = lambda i, j: data[i + 1][j]

    bassins = []
    for row_index in range(n_rows):
        for column_index in range(n_columns):
            actual = data[row_index][column_index]
            positions = []
            
            # got something left
            if column_index > 0:
                positions.append(get_left(row_index, column_index))
            # got something right
            if column_index < n_columns - 1:
                positions.append(get_right(row_index, column_index))
            # got something top
            if row_index > 0:
                positions.append(get_top(row_index, column_index))
            # got something bot
            if row_index < n_rows - 1:
                positions.append(get_bot(row_index, column_index))
            
            
            if len(positions) > 0 and actual < min(positions):
                bassins.append(Bassin(data, (row_index, column_index)))

    sizes = []
    for bassin in bassins:
        if len(sizes) < 3:
            l = len(bassin)
            sizes.append(l)
            
        else:
            sizes = sorted(sizes)
            l = len(bassin)
            if sizes[0] < l:
                sizes[0] = l

    return reduce(operator.mul, sizes)


def main():
    data = get_data()
    print(puzzle2(data))

if __name__ == '__main__':
    main()