

def get_data():
    s = '16,1,2,0,4,2,7,1,2,14'

    with open('day7_data.txt', 'r') as f:
        s = f.read()
    x = []
    for i in s.split(','):
        x.append(int(i))
    
    return x

def get_cost_puzzle1(i, data):
    sum = 0
    for d in data:
        sum += abs(d-i)

    return sum
    
def get_cost_puzzle2(i, data):
    sum = 0
    for d in data:
        temp = 0
        for j in range(1, abs(d-i)+1):
            temp += j
        sum += temp
    return sum

def puzzle1():
    data = get_data()

    most_left = min(data)
    most_right = max(data)

    print(f'[{most_left};{most_right}]')
    costs = {}

    for i in range(most_right+1 - most_left):
        print(f'{i} / {most_right}')
        costs[i] = get_cost_puzzle2(i, data)
    
    ret = min(costs.items(), key=lambda x: x[1])

    return ret 

def main():
    print(puzzle1())

if __name__ == '__main__':
    main()