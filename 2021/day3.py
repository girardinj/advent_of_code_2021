from numpy import *


def as_num(bits):
    bits.reverse()
    ret = 0
    for i in range(len(bits)):
        ret += pow(2, i) * int(bits[i])
    return ret

def puzzle1():
    bits = []
    with open('day3_data.txt') as f:
        for line in f:
            b = []
            for c in line:
                if c != '\n':
                    b.append(c)
            bits.append(b)

    zeros = [0 for i in range(len(bits[0]))]
    uns = [0 for i in range(len(bits[0]))]

    for value in bits:
        for i in range(len(value)):
            bit = int(value[i])
            if bit == 0:
                zeros[i] += 1
            elif bit == 1:
                uns[i] += 1
            else:
                print('error')
    
    most_bits = []

    for zero, un in zip(zeros, uns):
        if zero > un:
            most_bits.append(0)
        elif un > zero:
            most_bits.append(1)
        else:
            print('error2')
    
    f = lambda i: 0 if i == 1 else 1
    less_bits = [f(i) for i in most_bits]
    
    return as_num(most_bits) * as_num(less_bits)


def oxygen_criteria(arr, index):
    to_pop = []
    uns = 0
    zeros = 0

    for i in arr:
        if i[index] == '1':
            uns += 1
        elif i[index] == '0':
            zeros += 1
        else:
            print(f'error: {i[index]}')

    most = None
    if uns > zeros:
        most = 1
    elif zeros > uns:
        most = 0
    else:
        most = 1

    for i in range(len(arr)):
        if arr[i][index] != str(most):
            to_pop.append(i)

    to_pop.reverse()
    for pop in to_pop:
        arr.pop(pop)

    return arr



def co2_criteria(arr, index):
    if len(arr) == 1:
        return arr
    to_pop = []
    uns = 0
    zeros = 0

    for i in arr:
        if i[index] == '1':
            uns += 1
        elif i[index] == '0':
            zeros += 1
        else:
            print(f'error: {i[index]}')

    most = None
    if uns > zeros:
        most = 0
    elif zeros > uns:
        most = 1
    else:
        most = 0

    for i in range(len(arr)):
        if arr[i][index] != str(most):
            to_pop.append(i)

    to_pop.reverse()
    for pop in to_pop:
        arr.pop(pop)

    return arr



def puzzle2():
    bits = []
    with open('day3_data.txt') as f:
        for line in f:
            b = []
            for c in line:
                if c != '\n':
                    b.append(c)
            bits.append(b)


    oxygen_rating = bits.copy()
    for i in range(len(bits[0])):
        oxygen_rating = oxygen_criteria(oxygen_rating, i)

    co2_rating = bits.copy()
    
    for i in range(len(bits[0])):
        co2_rating2 = co2_criteria(co2_rating, i)
    
    if len(oxygen_rating) != 1:
        print('error with selection: oxygen')

    if len(co2_rating) != 1:
        print('error with selection: CO2')

    return as_num(oxygen_rating[0]) * as_num(co2_rating[0])

def main():
    print(puzzle2())

if __name__ == "__main__":
    main()