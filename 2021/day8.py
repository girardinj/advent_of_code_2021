
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
    for i in range(0, 10):
        numbers[i] = None
        
    for s in signal:
        l = len(s)

        if   l == 2: #1
            numbers[1] = set(s)
        elif l == 4: #4
            numbers[4] = set(s)
        elif l == 3: #7
            numbers[7] = set(s)
        elif l == 7: #8
            numbers[8] = set(s)
        
    
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
    for i in range(len(signal)):
        s = signal[i]
        if len(s) == 5:
            s = set(s)
            if numbers[7] == numbers[7].intersection(s):
                numbers[3] = s
                break

    # we can know b because of {4} inter ( {8 without 3} )
    b = numbers[4].intersection(numbers[8].difference(numbers[3]))
    assert len(b) == 1, f'error with b: {b}'

    # we can know 2 because len == 5, b not in {2} and {5} != {3}
    for i in range(len(signal)):
        s = signal[i]
        if len(s) == 5:
            s = set(s)
            if s != numbers[3] and len(b.intersection(s)) == 0:
                numbers[2] = s
                break


    # we can know 5 because len == 5, {5} != {2} and {5} != {3}
    for i in range(len(signal)):
        s = signal[i]
        if len(s) == 5:
            s = set(s)
            if s != numbers[2] and s != numbers[3]:
                numbers[5] = s
                break
    
    # we can know e because not in {5}, not in {1} but in {8}
    e = numbers[8].difference(numbers[5].union(numbers[1]))
    assert len(e) == 1, f'error with e: {e}'
    
    # we can know 9 because it is {8} without e
    numbers[9] = numbers[8].difference(e)

    # we can know 6 because len = 6, the one missing is in {1}
    for s in signal:
        if len(s) == 6:
            s = set(s)
            if len(numbers[1].intersection(numbers[8].difference(s))) == 1:
                numbers[6] = s
                break

    # we can know 0 because len = 6, and is not 6 neither 9
    for s in signal:
        if len(s) == 6:
            s = set(s)
            if s != numbers[6] and s != numbers[9]:
                numbers[0] = s
                break
        

    for k, n in numbers.items():
        if n == None:
            print(f'numbers not finished, {k} is None')
            exit(-1)
    
    # we know 0,1,2,3,4,5,7,8,9
    # we know a,b,e
    
    # c is in 8 but not in 6
    c = numbers[8].difference(numbers[6])
    assert len(c) == 1, f'error with c: {c}'

    # d is in 8 but not in 0
    d = numbers[8].difference(numbers[0])
    assert len(d) == 1, f'error with d: {d}'
    
    # f is in 1 but not in 2
    f = numbers[1].difference(numbers[2])
    
    # g is in 9 but not in (4+a+e)
    g = numbers[9].difference(numbers[4].union(a).union(e))

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

    space = '  '
    s = ''
    s += f'{space}{a}{a}{a}{space}\n'
    s += f'{b}{space}{space}{space}{space}{c}\n'
    s += f'{b}{space}{space}{space}{space}{c}\n'
    s += f'{space}{d}{d}{d}{space}\n'
    s += f'{e}{space}{space}{space}{space}{f}\n'
    s += f'{e}{space}{space}{space}{space}{f}\n'
    s += f'{space}{g}{g}{g}{space}\n'

    decoder = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g}

    for k,v  in decoder.items():
        for k2,v2 in decoder.items():
            if k == k2:
                continue
            assert v != v2, f'error, multiple values in decoder\n{decoder}'
    #   aaaa 
    #  b    c
    #  b    c
    #   dddd 
    #  e    f
    #  e    f
    #   gggg
    corresp = []
    corresp.append(set().union(decoder['a']).union(decoder['c']).union(decoder['f']).union(decoder['g']).union(decoder['e']).union(decoder['b'])) # 0
    corresp.append(set().union(decoder['c']).union(decoder['f'])) # 1
    corresp.append(set().union(decoder['a']).union(decoder['c']).union(decoder['d']).union(decoder['e']).union(decoder['g'])) # 2
    corresp.append(set().union(decoder['a']).union(decoder['c']).union(decoder['d']).union(decoder['f']).union(decoder['g'])) # 3
    corresp.append(set().union(decoder['b']).union(decoder['c']).union(decoder['d']).union(decoder['f'])) # 4
    corresp.append(set().union(decoder['a']).union(decoder['b']).union(decoder['d']).union(decoder['f']).union(decoder['g'])) # 5
    corresp.append(set().union(decoder['a']).union(decoder['b']).union(decoder['d']).union(decoder['e']).union(decoder['f']).union(decoder['g'])) # 6
    corresp.append(set().union(decoder['a']).union(decoder['c']).union(decoder['f'])) # 7
    corresp.append(set().union(decoder['a']).union(decoder['b']).union(decoder['c']).union(decoder['d']).union(decoder['e']).union(decoder['f']).union(decoder['g'])) # 8
    corresp.append(set().union(decoder['a']).union(decoder['b']).union(decoder['c']).union(decoder['d']).union(decoder['f']).union(decoder['g'])) # 9
    
    # print(s)
    # for i in range(len(corresp)):
    #     print(f'[{i}]: {corresp[i]}')
    return corresp


def compute(values, decoder):
    sum = 0
    for i in range(len(values)):
        sum += 10**(len(values)-1-i) * get_as_int(values[i], decoder)
    # print(sum)
    return sum

def get_as_int(value, decoder):
    v = set(value)
    # print(value)
    for i in range(len(decoder)):
        if v == decoder[i]:
            # print(i)
            return i
    return None

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
    