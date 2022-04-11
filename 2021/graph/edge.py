class Edge:
    """
    A class to represent an Edge.

    ...

    Attributes
    ----------
    value : Object
        Value of the edge
    v1 : Vertex
        First connected vertex
    v2 : Vertex
        Second connected vertex
    """

    def __init__(self, value, v1, v2):
        """
        Create an edge connected between two vertices, with a given value

        :param value: value of the Edge

        :param v1: first edge
        :type v1: Vertex

        :param v2: second vertex
        :type v2: Vertex
        """
        self.value = value
        self.v1 = v1
        self.v2 = v2

    def __eq__(self, o):
        """
        Compare the edge

        Edge compare its value and its two vertices

        :param o: the object to compare with
        """
        if type(o) != type(self):
            return False
        b = self.v1 == o.v1 and self.v2 == o.v2
        if not b:
            b = self.v1 == o.v2 and self.v2 == o.v1
        return self.value == o.value and b

    def __str__(self):
        """
        Describe the edge
        """
        return f'{self.v1} - {self.value} - {self.v2}'

    def get_other_vertex(self, vertex):
        """
        Given a vertex, return the other, or None
        
        :param v: the first vertex
        :type v: Vertex
        
        :returns: the other vertex, or None if the parameter is not connected
        :rtype: Vertex?
        """
        if self.v1 == vertex:
            return self.v2
        elif self.v2 == vertex:
            return self.v1
        return None
