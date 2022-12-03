import collections
import threading
import time

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
    # with open('day14_data.txt', 'r') as f:
    #     s = f.read()
    
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

def puzzle1(data, with_threads=True):
    polymer, rules = data

    threads = []
    time_start = time.time()
    for i in range(10):
        print('step', i)
        for i in range(len(rules)):
            if with_threads:
                threads.insert(i, threading.Thread(target = f, args=(polymer, rules[i])))
                threads[i].start()
            else:
                polymer.prepare_to_morph(rules[i])
        for t in threads:
            t.join()
        threads = []
        polymer.morph()
    time_end = time.time()
    
    s = polymer.compute()
    print('time:', time_end - time_start)
    return s

def generate_thing(data):
    pairs = {}
    old_c = data.pop(0)
    for c in data:
        if pairs.get(old_c + c) is None:
            pairs[old_c + c] = 1
        else:
            pairs[old_c + c] += 1
        old_c = c
    return pairs

def puzzle2(data, n):
    # data is stored like this:
    # for NNCB:
    # {'NN': 1, 'NC': 1, 'CB': 1}
    # for NNCBCBN:
    # {'NN': 1, 'NC': 1, 'CB': 2, 'BC': 1, 'BN': 1}
    polymer, rules = data
    data = polymer.data
    pairs = generate_thing(data)

    
    pairs_to_add = []
    for i in range(n):
        # search if a pair exists
        for rule in rules:
            pair = rule.left + rule.right
            if pairs.get(pair) is not None:
                pairs_to_add.append(rule)
        
        # extends the thing
        for rule in pairs_to_add:
            pair = rule.left + rule.right
            pairs[pair] -= 1
            if pairs[pair] == 0:
                del pairs[pair]
            pair_left = rule.left + rule.middle
            pair_right = rule.middle + rule.right
            
            if pairs.get(pair_left) is None:
                pairs[pair_left] = 1
            else:
                pairs[pair_left] += 1
            if pairs.get(pair_right) is None:
                pairs[pair_right] = 1
            else:
                pairs[pair_right] += 1
        
        pairs_to_add = []
    
    print(pairs)

def main():
    data = get_data()
    print(generate_thing([c for c in 'NBBBCNCCNBBNBNBBCHBHHBCHB']))
    
    print(puzzle2(data, 3))

if __name__ == '__main__':
    main()