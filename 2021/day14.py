import collections
import threading

def get_data():
    s = '''
        NNCB
        
        CH -> B
        HH -> N
        CB -> H
        NH -> C
        HB -> C
        HC -> B
        HN -> C
        NN -> C
        BH -> H
        NC -> B
        NB -> B
        BN -> B
        BB -> N
        BC -> B
        CC -> N
        CN -> C
        '''

    rules = []
    with open('day14_data.txt', 'r') as f:
        s = f.read()
    
    lines = s.strip().splitlines()
    polymer = Polymer_thing(lines.pop(0).strip())
    # remove blank
    lines.pop(0)
    for line in lines:
        rules.append(Rule(line.strip()))
    
    return (polymer, rules)

class Polymer_thing():
    def __init__(self, state):
        self.data = [c for c in state.strip()]
        self.to_morph = None
    
    def prepare_to_morph(self, rule):
        if self.to_morph is None:
            self.to_morph = {}
        
        for i in range(len(self.data) -1):
            if self.data[i] == rule.left and self.data[i+1] == rule.right:
                self.to_morph[i+1] = rule.middle
    
    def morph(self):
        assert self.to_morph is not None
        self.to_morph = collections.OrderedDict(sorted(self.to_morph.items()))
        counter = 0
        for k, v in self.to_morph.items():
            self.data.insert(k + counter, v)
            counter += 1
        self.to_morph = None
    
    def compute(self):
        chars = {}
        for c in self.data:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
        reverse_chars = {v: k for k, v in chars.items()}
        most_common_count = max(reverse_chars.keys())
        most_common = reverse_chars[most_common_count]
        least_common_count = min(reverse_chars.keys())
        least_common = reverse_chars[least_common_count]
        print('most common:', most_common, most_common_count)
        print('least common:', least_common, least_common_count)
        
        return most_common_count - least_common_count
    
    def __str__(self):
        return ''.join(self.data)

class Rule():
    def __init__(self, line):
        s = line.replace(' ', '').split('->')
        assert len(s[0]) == 2
        assert len(s[1]) == 1
        
        self.left = s[0][0]
        self.right = s[0][1]
        self.middle = s[1]
    
    def __str__(self):
        return f'{self.left}{self.right} -> {self.middle}'

def f(polymer, rule):
    polymer.prepare_to_morph(rule)

def puzzle1(data):
    polymer, rules = data

    threads = []
    for i in range(40):
        print('step', i)
        for i in range(len(rules)):
            threads.insert(i, threading.Thread(target = f, args=(polymer, rules[i])))
            threads[i].start()
        for t in threads:
            t.join()
        threads = []
        polymer.morph()
        
    
    s = polymer.compute()
    return s

def main():
    data = get_data()
    print(puzzle1(data))

if __name__ == '__main__':
    main()