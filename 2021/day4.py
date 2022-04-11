
class Grid():
    def __init__(self, size):
        self.grid = []
        self.grid_validated = []
        for _ in range(size):
            row = [-1 for _ in range(size)]
            self.grid.append(row)
            row_v = ['o' for _ in range(size)]
            self.grid_validated.append(row_v)


    def play(self, num):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[j][i] == num:
                    self.grid_validated[j][i] = 'x'
                    return self.check_if_won(i, j)
        return False, None

    def check_if_won(self, row_index, column_index):
        # check row
        b1 = True
        row = []
        for i in range(len(self.grid)):
            c = self.grid_validated[i][row_index]
            row.append(self.grid[i][row_index])
            if c != 'x':
                b1 = False
                break

        # check column
        b2 = True
        column = []
        for i in range(len(self.grid)):
            c = self.grid_validated[column_index][i]
            column.append(self.grid[column_index][i])
            if c != 'x':
                b2 = False
                break
        
        if b1:
            return True, row
        if b2:
            return True, column
        return False, None

    def get_sum(self):
        sum = 0

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid_validated[j][i] != 'x':
                    sum += self.grid[j][i]
                
        return sum

    def __str__(self):
        s = ''
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                capsule_left = '(' if self.grid_validated[j][i] == 'x' else ' '
                capsule_right = ')' if self.grid_validated[j][i] == 'x' else ' '
                s += f'{capsule_left}{self.grid[j][i]}{capsule_right} '
            s = s[:-1]
            s += '\n'
        s = s[:-1]
        return s

    def append(self, row, column, value):
        self.grid[column][row] = value

def puzzle1():

    numbers = None
    grids = []
    with open('day4_data.txt', 'r') as f:
        numbers = f.readline().split(',')
        numbers[len(numbers) -1] = numbers[len(numbers) -1].split('\n')[0]

        f.readline() # skip the empty first line
        size = 5
        grid = Grid(size)
        row_counter = 0
        column_counter = 0
        for line in f:
            if line == '\n':
                continue
        
            import re
            reg_num = r'(\d+)'
            x = re.findall(reg_num, line)
            if len(x) != size:
                print('error with len')

            for i in x:
                grid.append(row_counter, column_counter, int(i))
                column_counter += 1
            column_counter = 0
            row_counter += 1
            if row_counter == size:
                row_counter = 0
                grids.append(grid)
                grid = Grid(size)

    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

    # test
    # numbers = [
    #     7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1
    # ]
    # g = [
    # 22, 13, 17, 11,  0,
    #  8,  2, 23,  4, 24,
    # 21,  9, 14, 16,  7,
    #  6, 10,  3, 18,  5,
    #  1, 12, 20, 15, 19,

    #  3, 15,  0,  2, 22,
    #  9, 18, 13, 17,  5,
    # 19,  8,  7, 25, 23,
    # 20, 11, 10, 24,  4,
    # 14, 21, 16, 12,  6,

    # 14, 21, 17, 24,  4,
    # 10, 16, 15,  9, 19,
    # 18,  8, 23, 26, 20,
    # 22, 11, 13,  6,  5,
    #  2,  0, 12,  3,  7
    # ]
    # grids = []
    # counter = 0
    # grid = Grid(5)
    # for i in range(3*5):
    #     for j in range(5):
    #         grid.append(i%5, j, g[5*i + j])

    #     counter += 1
    #     if counter == 5:
    #         counter = 0
    #         grids.append(grid)
    #         grid = Grid(5)

        
    for num in numbers:
        for i in range(len(grids)):
            grid = grids[i]
            won, arr = grid.play(num)
            if (won):
                return num * grid.get_sum()
    return 'end'

def puzzle2():

    numbers = None
    grids = []
    with open('day4_data.txt', 'r') as f:
        numbers = f.readline().split(',')
        numbers[len(numbers) -1] = numbers[len(numbers) -1].split('\n')[0]

        f.readline() # skip the empty first line
        size = 5
        grid = Grid(size)
        row_counter = 0
        column_counter = 0
        for line in f:
            if line == '\n':
                continue
        
            import re
            reg_num = r'(\d+)'
            x = re.findall(reg_num, line)
            if len(x) != size:
                print('error with len')

            for i in x:
                grid.append(row_counter, column_counter, int(i))
                column_counter += 1
            column_counter = 0
            row_counter += 1
            if row_counter == size:
                row_counter = 0
                grids.append(grid)
                grid = Grid(size)

    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

    # test
    # numbers = [
    #     7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1
    # ]
    # g = [
    # 22, 13, 17, 11,  0,
    #  8,  2, 23,  4, 24,
    # 21,  9, 14, 16,  7,
    #  6, 10,  3, 18,  5,
    #  1, 12, 20, 15, 19,

    #  3, 15,  0,  2, 22,
    #  9, 18, 13, 17,  5,
    # 19,  8,  7, 25, 23,
    # 20, 11, 10, 24,  4,
    # 14, 21, 16, 12,  6,

    # 14, 21, 17, 24,  4,
    # 10, 16, 15,  9, 19,
    # 18,  8, 23, 26, 20,
    # 22, 11, 13,  6,  5,
    #  2,  0, 12,  3,  7
    # ]
    # grids = []
    # counter = 0
    # grid = Grid(5)
    # for i in range(3*5):
    #     for j in range(5):
    #         grid.append(i%5, j, g[5*i + j])

    #     counter += 1
    #     if counter == 5:
    #         counter = 0
    #         grids.append(grid)
    #         grid = Grid(5)

    for num in numbers:
        to_pop = []
        for i in range(len(grids)):
            grid = grids[i]
            won, arr = grid.play(num)
            if (won):
                to_pop.append(i)
                if len(grids) == 1:
                    print(grids[0])
                    print(num)
                    print(grids[0].get_sum())
                    return num * grids[0].get_sum()

        to_pop.reverse()
        for i in to_pop:
            grids.pop(i)
    return 'end'

def main():
    print(puzzle2())

if __name__ == '__main__':
    main()