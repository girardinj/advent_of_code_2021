
from copy import deepcopy
from turtle import st
from graph import Graph
import numpy as np

def get_data():
    s = '''
        start-A
        start-b
        A-c
        A-b
        b-d
        A-end
        b-end
        '''
    s = '''
        dc-end
        HN-start
        start-kj
        dc-start
        dc-HN
        LN-dc
        HN-end
        kj-sa
        kj-HN
        kj-dc
        '''
    s = '''
        fs-end
        he-DX
        fs-he
        start-DX
        pj-DX
        end-zg
        zg-sl
        zg-pj
        pj-he
        RW-he
        fs-DX
        pj-RW
        zg-RW
        start-pj
        he-WI
        zg-he
        pj-fs
        start-RW
        '''
    directions = []
    with open('day12_data.txt', 'r') as f:
        s = f.read()
    
    for line in s.strip().splitlines():
        line = line.strip()
        words = []
        for word in line.split('-'):
            words.append(word)
        directions.append(words)
    
    return directions

def dive(actual_cave, visited, end, joker_used=True, start=None):
    if actual_cave in visited:
        if not joker_used and actual_cave != start:
            joker_used = True
        else:
            return []
    
    if actual_cave == end:
        return [[actual_cave]]

    if not actual_cave.is_big_cave:
        visited = np.append(visited, actual_cave)
    
    pathes = []
    neighbours = [e.get_other_vertex(actual_cave) for e in actual_cave.get_edges()]
    for neighbour in neighbours:
        baby_pathes = dive(neighbour, visited.copy(), end, joker_used, start)
        for path in baby_pathes:
            path.insert(0, actual_cave)
            pathes.append(path)

    return pathes



def puzzle(data):
    graph = Graph()
    caves = {}
    
    for tunnel in data:
        v = []
        for i in range(2):
            try:
                vertex = caves[tunnel[i]]
            except:
                vertex = graph.add_value_as_vertex(tunnel[i])
                vertex.is_big_cave = tunnel[i] != tunnel[i].lower()
                
                caves[tunnel[i]] = vertex
            v.append(vertex)
                
        graph.connect_two_vertex(v[0], v[1], '')
    
    start = caves.pop('start')
    end = caves.pop('end')

    pathes = dive(start, np.array([]), end, False, start)

    return len(pathes)
    
    
        

def main():
    data = get_data()
    print(puzzle(data))

if __name__ == '__main__':
    main()
