

from importlib.resources import path


class Node:
    def __init__(self, value=None):
        self.value = value
    
    def __str__(self):
        return self.value


class Edge:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight


class Graph:
    def __init__(self):
        self._adjacency_list ={}

    def add_node(self, value):
        """ Arguments: value
            Returns: The added node
            Add a node to the graph
        """
        v = Node(value)
        self._adjacency_list[v] = [] #A LinkedList
        return v

    def add_edge(self, node1, node2, weight=0):
        """ Arguments: 2 nodes to be connected by the edge, weight (optional)
            Returns: nothing
            Adds a new edge between two nodes in the graph
            If specified, assign a weight to the edge
            Both nodes should already be in the Graph
        """
        if not node1 in self._adjacency_list.keys():
            raise KeyError("Node does not exist in adjacency list !")

        if not node2 in self._adjacency_list.keys():
            raise KeyError("Node does not exist in adjacency list !")
        
        edge = Edge(node2, weight=weight)
        self._adjacency_list[node1].append(edge)

    def get_nodes():
        """
            Arguments: none
            Returns all of the nodes in the graph as a collection (set, list, or similar)
        """

    def get_neighbors(node):
        """
            Arguments: node
            Returns a collection of edges connected to the given node
            Include the weight of the connection in the returned collection
        """

    def size():

        """ Arguments: none
            Returns the total number of nodes in the graph
        """
    
    def __str__(self):
        output = ''

        for vertex in self._adjacency_list.keys():
            output+= f'{vertex} ->'
            for edge in self._adjacency_list[vertex]:
                output += f'{edge.vertex}-->'
            output+='\n'
        
        return output


if __name__ == "__main__":

    graph = Graph()

    a=graph.add_node("A")
    b=graph.add_node("B")
    c=graph.add_node("C")
    d=graph.add_node("D")
    e=graph.add_node("E")
    f=graph.add_node("F")
    g=graph.add_node("G")

    graph.add_edge(a,d)
    graph.add_edge(a,c)
    graph.add_edge(a,b)
    graph.add_edge(b,c)
    graph.add_edge(e,b)
    graph.add_edge(c,f)
    graph.add_edge(f,g)
    graph.add_edge(f,e)

    # print(graph._adjacency_list)

    print(graph)

"""
a -> b -> c->d
a -> b -> c->d
a -> b -> c->d
"""


