
def puzzle1():
    horizontal = 0
    depth = 0

    reg_forward = r'forward (\d+)'
    reg_up = r'up (\d+)'
    reg_down = r'down (\d+)'

    import re
    with open('day2_input.txt', 'r') as f:
        for line in f:
            x = re.match(reg_forward, line)
            if x is not None:
                horizontal += int(x.group(1))
                continue
            x = re.match(reg_up, line)
            if x is not None:
                depth -= int(x.group(1))
                continue
            x = re.match(reg_down, line)
            if x is not None:
                depth += int(x.group(1))
                continue
            print('error')

    return horizontal * depth

def puzzle2():
    horizontal = 0
    depth = 0
    aim = 0

    reg_forward = r'forward (\d+)'
    reg_up = r'up (\d+)'
    reg_down = r'down (\d+)'

    import re
    with open('day2_input.txt', 'r') as f:
        for line in f:
            x = re.match(reg_forward, line)
            if x is not None:
                horizontal += int(x.group(1))
                depth += int(x.group(1))*aim
                continue
            x = re.match(reg_up, line)
            if x is not None:
                aim -= int(x.group(1))
                continue
            x = re.match(reg_down, line)
            if x is not None:
                aim += int(x.group(1))
                continue
            print('error')
            break

    return horizontal * depth

def main():
    print(puzzle2())

if __name__ == '__main__':
    main()