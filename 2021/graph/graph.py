from .edge import Edge
from .vertex import Vertex

class Graph:
    """
    A class to represent a graph.

    ...

    Attributes
    ----------
    vertices : Vertex[]
        Array of vertices
    edges : Edges[]
        Array of edges
    """
    
    def __init__(self):
        self.edges = []
        self.vertices = []

    def add_value_as_vertex(self, value) -> Vertex:
        """
        Create a new node with the given value

        :param value: the value of the new node

        :returns: the newly created vertex
        :rtype: Vertex
        """
        ret = Vertex(value)
        self.vertices.append(ret)
        return ret

    '''
    def add_and_connect_vertex(self, new_vertex, old_vertex, value_of_edge):
        new = Vertex(new_value)
        edge = Edge(value_of_edge, old_vertex, new_vertex)
        
        new_vertex.add_edge(edge)
        old_vertex.add_edge(edge)

        self.vertices.append(new_vertex)
    '''

    def connect_two_vertex(self, v1: Vertex, v2: Vertex, value_of_edge) -> Edge:
        """
        Create a connection between two nodes

        :param v1: the first node
        :type v1: Vertex

        :param v2: the second node
        :type v2: Vertex

        :param value_of_edge: the value to add to the connection

        :returns: the new edge
        :rtype: Edge
        """
        edge = Edge(value_of_edge, v1, v2)

        self.edges.append(edge)
        
        v1.add_edge(edge)
        v2.add_edge(edge)

        return edge    

    def find_vertex_from_value(self, value) -> Vertex:
        """
        Get a node from its value

        :param value: the value to search

        :returns: the node
        :rtype: Vertex
        """
        for v in self.vertices:
            if v.value == value:
                return v
        return None

    def find_edge_from_value(self, value) -> Edge:
        """
        Get a connection from its value

        :param value: the value to search

        :returns: the connection
        :rtype: Edge
        """
        for edge in self.edges:
            if edge.value == value:
                return edge
        return None
    
    def find_edge_from_vertexes(self, v1: Vertex, v2: Vertex) -> Edge:
        """
        Get a connection from its two nodes

        :param v1: the first node
        :type v1: Vertex

        :param v2: the second node
        :type v2: Vertex

        :returns: the connection, or None if the nodes are not connected
        :rtype: Edge?
        """
        for edge in self.edges:
            if edge.v1 == v1 and edge.v2 == v2:
                return edge
            if edge.v1 == v2 and edge.v2 == v1:
                return edge
        return None

    def has_node_value(self, value) -> bool:
        """
        Know if there is a node with the given value in the graph

        :param value: the value to compare

        :returns: if the graph contains a node with the given value
        :rtype: bool
        """
        for v in self.vertices:
            if v.value == value:
                return True
        return False

    def has_node(self, vertex: Vertex) -> bool:
        """
        Know if there is a node in the graph

        :param vertex: the node to search

        :returns: if the graph contains the node
        :rtype: bool
        """
        for v in self.vertices:
            if v == vertex:
                return True
        return False

    def has_connection_value(self, value) -> bool:
        """
        Know if there is a connection with the given value in the graph

        :param value: the value to compare

        :returns: if the graph contains a connection with the given value
        :rtype: bool
        """
        for e in self.edges:
            if e.value == value:
                return True
        return False

    def has_connection(self, edge: Edge) -> bool:
        """
        Know if there is a connection in the graph

        :param edge: the connection to search

        :returns: if the graph contains the connection
        :rtype: bool
        """
        for e in self.edges:
            if e == edge:
                return True
        return False

    def __str__(self) -> str:
        """
        Output the graph as a string
        
        :returns: the text representation of the graph
        :rtype: str
        """
        ret = ''

        for v in self.vertices:
            ret += f'vertex: {v.value}\n'
            for e in v.edges:
                ret += f'--> {e.get_other_vertex(v).value} | {e.value}\n'

        return ret
