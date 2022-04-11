

from operator import is_
from tkinter.messagebox import NO


def get_data():
    s = '''
    [({(<(())[]>[[{[]{<()<>>
    [(()[<>])]({[<{<<[]>>(
    {([(<{}[<>[]}>{[]{[(<()>
    (((({<>}<{<{<>}{[]{[]{}
    [[<[([]))<([[{}[[()]]]
    [{[{({}]{}}([{[{{{}}([]
    {<[[]]>}<{[{[{[]{()[[[]
    [<(<(<(<{}))><([]([]()
    <{([([[(<>()){}]>(<<{{
    <{([{{}}[<[[[<>{}]]]>[]]
    '''
    with open('day10_data.txt', 'r') as f:
        s = f.read()
    s.strip()
    ret = []
    illegal_char = ['', ' ', '\t']
    for line in s.splitlines():
        sline = ''
        for c in line:
            if c not in illegal_char:
                sline += c
        if len(sline) > 0:
            ret.append(sline)
    return ret

def corrupted_line(line):
    l = len(line)
    char_open = ['(', '[', '{', '<']
    char_close = [')', ']', '}', '>']
    chars = []
    for i in range(l):
        c = line[i]
        if c in char_open:
            chars.append(c)
        elif c in char_close:
            c_open = chars.pop()
            if c_open == '(' and c != ')':
                return True, ')', c, None
            if c_open == '[' and c != ']':
                return True, ']', c, None
            if c_open == '{' and c != '}':
                return True, '}', c, None
            if c_open == '<' and c != '>':
                return True, '>', c, None
        else:
            assert False, f'invalid char: {line[i]}'
    
    return False, None, None, chars

def get_corrupted_score(chars):
    score = 0
    for c in chars:
        if c == ')':
            score += 3
        elif c == ']':
            score += 57
        elif c == '}':
            score += 1197
        elif c == '>':
            score += 25137
        else:
            assert False, f'invalid char {c}'
    return score

def get_incomplete_score(incomplete_lines):
    scores = []
    for line in incomplete_lines:
        line = reversed(line)
        score = 0
        for c in line:
            score *= 5
            if c == '(':
                score += 1
            elif c == '[':
                score += 2
            elif c == '{':
                score += 3
            elif c == '<':
                score += 4
            else:
                assert False, f'invalid char {c}'
        scores.append(score)
    
    scores = sorted(scores)
    if len(scores) % 2 == 0:
        print('possible error')
        return (scores[len(scores) // 2] + scores[len(scores) // 2 - 1]) / 2
    else:
        return scores[len(scores) // 2]

def puzzle(data):
    corrupted_lines_char = []
    incomplete_lines_chars = []
    for i in range(len(data)):
        line = data[i]
        
        is_corrupted, c_open, c_close, remaining_open = corrupted_line(line)
        if is_corrupted:
            corrupted_lines_char.append(c_close)
            # print(f'line {i} is corrupted: {line}, expected {c_open} but found {c_close} instead')
        # if is incomplete
        elif len(remaining_open) != 0:
            incomplete_lines_chars.append(remaining_open)
    
    # score = get_corrupted_score(corrupted_lines_char)
    score = get_incomplete_score(incomplete_lines_chars)
    return score

def main():
    data = get_data()
    print(puzzle(data))
    
if __name__ == '__main__':
    main()