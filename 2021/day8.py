
'''
digit :

 aaaa
b    c
b    c
 dddd
e    f
e    f
 gggg
'''

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
            or len(d) == 7): # 7
            sum += 1
    
    return sum

def decode(signal):
    decoder = {}
    return decoder

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
    