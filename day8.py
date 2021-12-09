
def get_data():
    s = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''

    with open('day8_data.txt', 'r') as f:
        s = f.read()

    signal = []
    output = []
    import re
    for s2 in s.split('\n'):
        reg = re.match(r'(.*)\|(.*)', s2)
        row_signal = []
        row_output = []
        for s3 in reg.groups()[0].split(' '):
            if len(s3) == 0:
                continue
            row_signal.append(s3)
        for s3 in reg.groups()[1].split(' '):
            if len(s3) == 0:
                continue
            row_output.append(s3)
        signal.append(row_signal)
        output.append(row_output)
    return signal, output


def puzzle1():
    _, data = get_data()

    sum = 0
    for d in data:
        if (len(d) == 2      # 1
            or len(d) == 4   # 4
            or len(d) == 3   # 7
            or len(d) == 7): # 8
            sum += 1
    
    return sum

def decode(signal):

    numbers = {}
    for i in range(0, 9):
        numbers[i] = None
    
    to_remove = []
    for i in range(len(signal)):
        s = signal[i]
        l = len(s)

        if   l == 2: #1
            numbers[1] = set(s)
            to_remove.append(i)
        elif l == 4: #4
            numbers[4] = set(s)
            to_remove.append(i)
        elif l == 3: #7
            numbers[7] = set(s)
            to_remove.append(i)
        elif l == 7: #8
            numbers[8] = set(s)
            to_remove.append(i)
        
    to_remove.reverse()
    for i in to_remove:
        signal.pop(i)
    
    # we found the sure numbers, now try to find the others
    '''
    0:      1:      2:      3:      4:
     aaaa    ....    aaaa    aaaa    ....
    b    c  .    c  .    c  .    c  b    c
    b    c  .    c  .    c  .    c  b    c
     ....    ....    dddd    dddd    dddd
    e    f  .    f  e    .  .    f  .    f
    e    f  .    f  e    .  .    f  .    f
     gggg    ....    gggg    gggg    ....

    5:      6:      7:      8:      9:
     aaaa    aaaa    aaaa    aaaa    aaaa
    b    .  b    .  .    c  b    c  b    c
    b    .  b    .  .    c  b    c  b    c
     dddd    dddd    ....    dddd    dddd
    .    f  e    f  .    f  e    f  .    f
    .    f  e    f  .    f  e    f  .    f
     gggg    gggg    ....    gggg    gggg
    '''

    # 2,3,5 len of 5
    # 0,6,9 len of 6

    # we know a because of {7} without {1}
    a = numbers[7].difference(numbers[1])
    assert len(a) == 1, f'error with a: {a}'

    # we can know 3 because {3} len of 5 and has {7}
    to_pop = None
    for i in range(len(signal)):
        s = signal[i]
        if len(s) == 5:
            s = set(s)
            if numbers[7] == numbers[7].intersection(s):
                numbers[3] = s
                to_pop = i
                break
    signal.pop(to_pop)

    # we can know b because of {4} inter ( {8 without 3} )
    b = numbers[4].intersection(numbers[8].difference(numbers[3]))
    assert len(b) == 1, f'error with b: {b}'

    # we can know {5} because len == 5, b not in {5} and {5} != {3}
    to_pop = None
    for i in range(len(signal)):
        s = signal[i]
        if len(s) == 5:
            s = set(s)
            if s != numbers[3] and len(b.intersection(s)) == 0:
                to_pop = i
                numbers[5] = s
                break
    signal.pop(to_pop)

    # we can know e because not in {5}, not in {1} but in {8}
    e = numbers[8].difference(numbers[5]).difference(numbers[1])
    assert len(e) == 1, f'error with e: {e}'

    # we can know 2 because len == 5, {2} != {3} and {2} != {5}
    to_pop = None
    for i in range(len(signal)):
        s = signal[i]
        if len(s) == 5:
            s = set(s)
            if s != numbers[3] and s != numbers[5]:
                to_pop = i
                numbers[2] = s
                break
    signal.pop(to_pop)
    
    # we can know 6 because len == 6 and {6} has {2}
    # we can know 9 because len == 6 and {9} has not e
    # we can know 0 because len == 6 and is the last

    for i in range(len(signal)):
        s = signal[i]
        if len(s) == 6:
            s = set(s)
            
            if numbers[2] == numbers[2].intersection(s):
                numbers[6] = s
            elif len(e.intersection(s)) == 0:
                numbers[9] = s
            else:
                numbers[0] = s
        else:
            print('error with what is in signal')
            exit(0)

    i = 0
    for v in numbers.values():
        if v == None:
            print('numbers not finished')
            exit(0)
        print(f'{i} is {v}')
        i += 1
    
    '''
    0:      1:      2:      3:      4:
     aaaa    ....    aaaa    aaaa    ....
    b    c  .    c  .    c  .    c  b    c
    b    c  .    c  .    c  .    c  b    c
     ....    ....    dddd    dddd    dddd
    e    f  .    f  e    .  .    f  .    f
    e    f  .    f  e    .  .    f  .    f
     gggg    ....    gggg    gggg    ....

    5:      6:      7:      8:      9:
     aaaa    aaaa    aaaa    aaaa    aaaa
    b    .  b    .  .    c  b    c  b    c
    b    .  b    .  .    c  b    c  b    c
     dddd    dddd    ....    dddd    dddd
    .    f  e    f  .    f  e    f  .    f
    .    f  e    f  .    f  e    f  .    f
     gggg    gggg    ....    gggg    gggg
    '''

    # so far, we know a, b and e

    # c in {1} inter {2}
    c = numbers[1].intersection(numbers[2])
    assert len(c) == 1, f'error with c: {c}'

    # d in {8} but not in {0}
    d = numbers[8].difference(numbers[0])
    assert len(d) == 1, f'error with d: {d}'

    # f in {1} inter {5}
    f = numbers[1].intersection(numbers[5])
    assert len(f) == 1, f'error with f: {f}'

    # g in (8 - (a+b+c+d+e+f))
    g = numbers[8].difference(a).difference(b).difference(c).difference(d).difference(e).difference(f)

    p = lambda k, v: print(f'{k} is {v}')

    s= ''
    s+= f'  {a}{a}{a}{a}\n'
    s+= f'{b}              {c}\n'
    s+= f'{b}              {c}\n'
    s+= f'  {d}{d}{d}{d}\n'
    s+= f'{e}              {f}\n'
    s+= f'{e}              {f}\n'
    s+= f'  dddddddddddddddd\n'
    print(s)
    print('error with either number 2 or number 3 or number 5 (for valueb or e')
    assert len(g) == 1, f'error with g: {g}'

    print(a, b, c, d, e, f, g)
    exit(0)


def compute(values, decoder):
    decoder.reverse()
    sum = 0
    for i in range(len(values)):
        sum += 10**i * get_as_int(values[i], decoder)
    return sum

def get_as_int(value, decoder):
    return value

def puzzle2():
    signal, output = get_data()

    sum = 0
    for s, o in zip(signal, output):
        d = decode(s)
        sum += compute(o, d)

    return sum


def main():
    print(puzzle2())

if __name__ == '__main__':
    main()
    