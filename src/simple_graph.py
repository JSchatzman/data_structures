"""Implementation of a simple graph in Python."""


class Graph(object):
    """Implementation of a simple directed Graph.

    g.nodes(): return a list of all nodes in the graph.

    g.edges(): return a list of all edges in the graph.

    g.add_node(n): adds a new node n to the graph.

    g.add_edge(n1, n2): adds a new edge to the graph connecting n1 and n2,
     if either n1 or n2 are not already present in the graph,
     they should be added.

    g.del_node(n): deletes the node n from the graph, raises an error
     if no such node exists

    g.del_edge(n1, n2): deletes the edge connecting n1 and n2 from the
     graph, raises an error if no such edge exists

    g.has_node(n): True if node n is contained in the graph,
     False if not.

    g.neighbors(n): returns the list of all nodes connected to n by
     edges, raises an error if n is not in g

    g.adjacent(n1, n2): returns True if there is an edge connecting n1
     and n2, False if not, raises an error if either of the supplied nodes
     are not in g

    """

    def __init__(self, data=None):
        """Initialize a graph instance.

        Data is the key of the dict and edges are held in a list of names.
        """
        self.graph = {}
        if data:
            for i in data:
                self.add_node(i)

    def nodes(self):
        """Return a list of all nodes in graph."""
        return [key for key in self.graph.keys()]

    def edges(self):
        """Return a list of all edges in the graph."""
        return [val for val in self.graph.values()]

    def add_node(self, node):
        """Add a new node to graph."""
        self.graph.setdefault(node, [])

    def add_edge(self, node1, node2):
        """Add an edge between node1 and node2."""
        self.graph.setdefault(node1, [])
        self.graph.setdefault(node2, [])
        self.graph[node1].append(node2)


    # del_node:
        # try:
        #   delete key in dict
        #   if node in self.edges():
                 # delete any references in list of edges for other keys
        # except ValueError:
            # raise value error if not there


    # del_edge(node1, node2):
        # find node1 in keys of dictionary
        # delete node 2 in list --> list remove function
        # raise value error if not there


    # has_node(node):
        # return node in self.nodes()
        # should return true if in list and false if not


    # neighbours(node):
        # return edges for input node
            # return self.graph[node]
        # else: raise value error?


    # adjacent(node1, node2):
        # find node 1 key and check if node2 is in value list
            # try:
                # return node2 in self.graph[node1]
            # except ValueError:
                # raise ValueError('node is not in the graph')




