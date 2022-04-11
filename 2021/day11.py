import colorama
colorama.init()

class Cutie_octopus():
    no_flashes = 0
    def __init__(self, initial_value):
        self.neighbors = []
        self.value = initial_value
        self.is_flashing = self.value > 9
    
    def init_neighbors(self, grid, row, col):
        if row > 0:
            self.neighbors.append(grid[row -1][col])
        if row < len(grid) - 1:
            self.neighbors.append(grid[row + 1][col])
        if col > 0:
            self.neighbors.append(grid[row][col - 1])
        if col < len(grid[0]) - 1:
            self.neighbors.append(grid[row][col + 1])
        if row > 0 and col > 0:
            self.neighbors.append(grid[row - 1][col - 1])
        if row > 0 and col < len(grid[0]) - 1:
            self.neighbors.append(grid[row - 1][col + 1])
        if row < len(grid) - 1 and col > 0:
            self.neighbors.append(grid[row + 1][col - 1])
        if row < len(grid) - 1 and col < len(grid[0]) - 1:
            self.neighbors.append(grid[row + 1][col + 1])
    
    def __str__(self) -> str:
        ret = str(self.value)
        if self.value == 0:
            ret = colorama.Fore.RED + ret + colorama.Fore.RESET
        return ret
    
    def __add__(self, value):
        if self.is_flashing:
            return
        self.value += value
        if self.value > 9:
            self.is_flashing = True
            Cutie_octopus.no_flashes += 1
            self.value = 0
            for neighbor in self.neighbors:
                neighbor += value
    
    def stop_flashing(self):
        self.is_flashing = False

def get_data():
    s = '''
    5483143223
    2745854711
    5264556173
    6141336146
    6357385478
    4167524645
    2176841721
    6882881134
    4846848554
    5283751526
    '''
    
    with open('day11_data.txt', 'r') as f:
        s = f.read()
    
    ret = []
    for line in s.strip().splitlines():
        ret.append(line.strip())
    return ret

def puzzle(data):
    octopuses = []
    for row in data:
        octopuses_row = []
        for value in row:
            value = int(value)
            octopuses_row.append(Cutie_octopus(int(value)))
        octopuses.append(octopuses_row)

    for row in range(len(octopuses)):
        for col in range(len(octopuses[0])):
            octopuses[row][col].init_neighbors(octopuses, row, col)
    
    print('initial state:')
    for octopuses_row in octopuses:
        for octopus in octopuses_row:
            print(octopus, end=' ')
        print()

    # puzzle 1
    # for _ in range(100):
    #     # increase
    #     for octopuses_row in octopuses:
    #         for octopus in octopuses_row:
    #             octopus += 1
    #     # reset flashing state
    #     for octopuses_row in octopuses:
    #         for octopus in octopuses_row:
    #             octopus.stop_flashing()
                
    # puzzle 2
    is_synchronizing = False
    steps = 0
    while not is_synchronizing:
        steps += 1
        # increase
        for octopuses_row in octopuses:
            for octopus in octopuses_row:
                octopus += 1
        # reset flashing state
        is_synchronizing = True
        for octopuses_row in octopuses:
            for octopus in octopuses_row:
                octopus.stop_flashing()
                # verify if synchronizing
                if octopus.value != 0:
                    is_synchronizing = False
    
    print('\nfinal state')
    for octopuses_row in octopuses:
        for octopus in octopuses_row:
            print(octopus, end=' ')
        print()
    
    # return steps + 10 - octopuses[0][0].value
    
    print(f'with a total of {Cutie_octopus.no_flashes} flashes, in {steps} steps')
    
    return Cutie_octopus.no_flashes

def main():
    data = get_data()
    print(puzzle(data))

if __name__ == '__main__':
    main()
