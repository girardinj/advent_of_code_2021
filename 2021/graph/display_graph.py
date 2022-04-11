import graphviz

def brother_in_array(path, v1, v2):

    i = 0
    while i < len(path):
        if path[i].value == v1:
            break
        i += 1

    if i >= len(path):
        return False
    
    if i+1 < len(path) and path[i+1].value == v2:
        return True

    if i-1 >= 0 and path[i-1].value == v2:
        return True

    return False

def in_path(path, v):
    for state in path:
        if v == state.value:
            return True
    return False


def print_graph(graph, path, starting_node, ending_node, print_with_pos=False, ratio=70, format='pdf', name='truite'):
    
    colors = {'lambda': 'black', 'start': 'blue', 'end': 'green', 'path': 'red'}

    dot = graphviz.Graph(name=name, comment='salut', format=format, engine='neato')
    #dot = graphviz.Digraph(name=name, comment='salut', format=format, engine='neato') DIgraph -> directed graph

    dic = {}
    i = 0
    
    total_length = 0

    for e in graph.edges:
        vertices = (e.v1.value, e.v2.value)
        for vertex in vertices:
            if vertex not in dic.keys():
                dic[vertex] = i
                label = f'{vertex}'
                if print_with_pos:
                    pos = f'{float(vertex.x)/ratio}, {float(vertex.y)/ratio}!'
                if starting_node != None and vertex == starting_node.value:
                    color = colors['start']
                elif ending_node != None and vertex == ending_node.value:
                    color = colors['end']
                else:
                    color = colors['lambda']
                
                if print_with_pos:
                    dot.node(name=str(i), label=label, pos=pos, color=color)
                else:
                    dot.node(name=str(i), label=label, color=color)
                i += 1

        if brother_in_array(path, e.v1, e.v2):
            color = colors['path']
            total_length += e.value
        else:
            color = colors['lambda']

        dot.edge(
            str(dic[e.v1.value]),
            str(dic[e.v2.value]),
            str(e.value),
            color=color
            )

    for v in graph.vertices:
        vertex = v.value
        if vertex in dic.keys():
            continue
        label = f'{vertex}'
        if print_with_pos:
            pos = f'{float(vertex.x)/ratio}, {float(vertex.y)/ratio}!'
        if starting_node != None and vertex == starting_node.value:
            color = colors['start']
        elif ending_node != None and vertex == ending_node.value:
            color = colors['end']
        else:
            color = colors['lambda']
        
        if print_with_pos:
            dot.node(name=str(i), label=label, pos=pos, color=color)
        else:
            dot.node(name=str(i), label=label, color=color)
        i += 1


    try:
        dot.render(filename=f'{name}.gv', view=False)
    except:
        print('################')
        print('graphviz must be installed and the bin folder added to your Environnement Var to have the pdf generated')
        print('https://graphviz.org/download/')
        print('################\n')
        
    # didn't find how to add title to graph, with the value
    return total_length


def print_console_path(result, graph, distance, completion):
    if completion:
        old = result.pop(0)
        print(f'start from : {old}')
        for node in result:
            print(f'go there   : {node} | {graph.find_edge_from_vertexes(node, old).value}')
            old = node
        print('\nYou have arrived !\n')
        print(f'total distance: {distance}')
    else:
        print('no path found...') 
