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



    References:
    https://www.python.org/doc/essays/graphs/
    https://medium.freecodecamp.com/a-gentle-introduction-to-data-structures-how-graphs-work-a223d9ef8837#.6xbpr1l6q
    http://stackoverflow.com/questions/19472530/representing-graphs-data-structure-in-python
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
        return [val for val in self.graph.values() if len(val) > 0]

    def add_node(self, node):
        """Add a new node to graph."""
        self.graph.setdefault(node, [])

    def add_edge(self, node1, node2):
        """Add an edge between node1 and node2."""
        self.graph.setdefault(node1, [])
        self.graph.setdefault(node2, [])
        if node2 not in self.graph[node1]:
            self.graph[node1].append(node2)

    def del_node(self, node):
        """Delete the inputted node from the graph."""
        if node not in self.graph:
            raise IndexError('The input node is not in the graph')
        del self.graph[node]
        for edge_list in self.graph.values():
            if node in edge_list:
                edge_list.remove(node)

    def del_edge(self, node1, node2):
        """Delete the edge connecting node1 to node 2 if it exists."""
        if node2 not in self.graph[node1]:
            raise IndexError('This edge does not exist.')
        self.graph[node1].remove(node2)

    def has_node(self, node):
        """Return true if the input node is in the graph, else False."""
        return node in self.graph

    def neighbours(self, node):
        """Return the list of nodes connected to the input node."""
        return self.graph[node]

    def adjacent(self, node1, node2):
        """Return True if there is an edge connecting n1 and n2."""
        if node1 not in self.graph or node2 not in self.graph:
            raise KeyError('One or both of these nodes is not in the graph.')
        return node2 in self.graph[node1]

    def depth_traversal(self, root, discovered=None):
        """Perform depth traversal of graph."""
        if discovered is None:
            discovered = []
        discovered.append(root)
        for edge in self.graph[root]:
            if edge not in discovered:
                self.depth_traversal(edge, discovered)
        return discovered

    def breadth_traversal(self, root):
        """Perform breath traversal of graph."""
        discovered = [root]
        node_edges = self.graph[root]
        while node_edges:
            edge = node_edges.pop(0)
            if edge not in discovered:
                discovered.append(edge)
                unique_edges = [i for i in self.graph[edge] if i not in discovered]
                node_edges.extend(unique_edges)
        return discovered
