
days_to_reproduce = 6 # 7 days => [6; 0]
days_to_reproduce_when_born = 8

lanternFishes = []

class LanternFish():
    def __init__(self, timer):
        self.internal_timer = timer

    def day_passed(self):
        self.internal_timer -= 1
        if self.internal_timer < 0:
            self.reproduce()
            self.internal_timer = days_to_reproduce

    def reproduce(self):
        lanternFishes.append(LanternFish(days_to_reproduce_when_born))

    def __str__(self):
        return self.internal_timer

def get_data():
    # s = '3,4,3,1,2'
    with open('day6_data.txt', 'r') as f:
        s = f.read()
    x = []
    for _s in s.split(','):
        x.append(int(_s))
    return x
    

def get_array():
    s = ''
    for lanternFish in lanternFishes:
        s += f'{lanternFish.internal_timer}, '
    s = s[:-2]
    return s

def puzzle1():
    days = 80
    data = get_data()

    for i in data:
        lanternFishes.append(LanternFish(i))

    # print('Initial state:', get_array())

    for i in range(days):
        print('day', i)
        l = len(lanternFishes)
        for j in range(l):
            lanternFishes[j].day_passed()
        
        # print(f'After {i+1} days:', get_array())

    return len(lanternFishes)

def puzzle2():
    values = {}
    days = 256
    for i in range(9):
        values[i] = 0
    data = get_data()
    for d in data:
        values[d] += 1
    print(values)
    for i in range(days):
        print('day', i)
        new_fish = 0
        for key in values.keys():
            if key == 0:
                new_fish = values[key]
            else:
                values[key-1] = values[key]
        values[days_to_reproduce_when_born] = new_fish
        values[days_to_reproduce] += new_fish

    sum = 0
    for v in values.values():
        sum += v
    return sum

def main():
    print(puzzle2())

if __name__ == "__main__":
    main()