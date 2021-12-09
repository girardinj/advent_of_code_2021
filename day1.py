import re

def puzzle1():
    differs = 0
    with open('day1_data.txt') as f:
        old = int(f.readline())
        for line in f:
            new = int(line)
            if old < new:
                differs += 1
            old = new
    
    return differs


def puzzle2():
    differs = 0
    with open('day1_data.txt') as f:
        old1 = int(f.readline())
        old2 = int(f.readline())
        old3 = int(f.readline())

        for line in f:
            new = int(line)
            
            old_old = old1 + old2 + old3
            
            old1 = old2
            old2 = old3
            old3 = new

            old_new = old1 + old2 + old3

            if old_old < old_new:
                differs += 1
    
    return differs

def main():
    print(puzzle2())

if __name__ == '__main__':
    main()