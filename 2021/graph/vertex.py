class Vertex:
    """
    A class to represent a Vertex.

    ...

    Attributes
    ----------
    value : Object
        Value of the vertex
    edges : Edge[]
        Array of connected edges
    """
    
    def __init__(self, value):
        """
        Create a new Vertex with a given value

        :param value: the value of the vertex
        """
        self.value = value
        self.edges = []

    def add_edge(self, edge, force: bool = False):
        """
        Connect an edge to the vertex

        :param edge: the edge to add to the vertex
        :type edge: Edge

        :param force: indicate if it should add it anyway, or check first if the edge is already connected
            (default is False)
        :type force: bool
        """

        if force or edge not in self.edges:
            self.edges.append(edge)

    def remove_edge(self, edge):
        """
        Remove the connection between the edge and the connection

        :param edge: the edge we want to remove
        :type edge: Edge
        """
        if edge in self.edges:
            self.edges.remove(edge)

    def __eq__(self, o) -> bool:
        """
        Compare the Vertex

        Vertex compare its value and its connections

        :param o: the object to compare with

        :returns: the comparison
        :rtype: bool
        """
        if type(o) != type(self):
            return False
        return self.value == o.value and self.edges == o.edges

    def __str__(self) -> str:
        """
        Describe the vertex
        """
        return str(self.value)

    def get_edges(self) -> list:
        """
        Get the connections of the vertex

        :returns: an array of its connections
        :rtype: Edges[]
        """
        return self.edges
