
# Nodes are pretty much the same as they were in trees.
# Instead of having a set number of children, each node has a list of Edges
class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []

# an edge connects two nodes
# it can also have a weight
class Edge:
    def __init__(self, weight, node_from, node_to):
        self.node_from = node_from
        self.node_to = node_to
        self.weight = weight

# the graph data structure encompasses all it's edges and nodes
# here we are assuming that nodes contain unique value
class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def insert_node(self, new_node_val):
        '''inserts a new node into the graph'''

        new_node = Node(new_node_val)
        self.nodes.append(new_node)

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        '''inserts an edge connecting two nodes into the graph'''

        # first we search for node_from and node_to Nodes which are connected by this edge
        node_from = None
        node_to = None
        for node in self.nodes:
            if node.value == node_from_val:
                node_from = node
            if node.value == node_to_val:
                node_to = node

        # even after the search, if we do not found them,
        # then they are not present and we need to create them
        if node_from is None:
            node_from = Node(node_from_val)
            self.nodes.append(node_from)
        if node_to is None:
            node_to = Node(node_to_val)
            self.nodes.append(node_to)

        # now that we're done with the nodes,
        # let's create the edge and insert it into our graph
        # remember, we also need to append this edge to the nodes it connects
        new_edge = Edge(new_edge_val, node_from, node_to)
        node_from.edges.append(new_edge)
        node_to.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""

        # we append the edge attributes to a list and return it
        edge_list = []
        for edge in self.edges:
            attributes = (edge.weight, edge.node_from.value, edge.node_to.value)
            edge_list.append(attributes)

        return edge_list

    def get_adjacency_list(self):
        """Don't return any Node or Edge objects!
        You'll return a list of lists.
        The indices of the outer list represent
        "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""

        # the size of the adjacency list will be equal to the max node value
        adjacency_list = [None] * (self.get_max_node_value()+1)
        # now we traverse through each edge (get_edge_list) and append it's weight and node_to into our adjacency list
        # the indices will represent our node_from values
        for edge in self.get_edge_list():
            node_from_val = edge[1]
            node_to_val = edge[2]
            weight = edge[0]
            if adjacency_list[node_from_val] is None:
                adjacency_list[node_from_val] = [(node_to_val, weight)]
            else:
                adjacency_list[node_from_val].append((node_to_val, weight))
        return adjacency_list

    def get_adjacency_matrix(self):
        '''returns the adjacency matrix'''

        # let's initialise the adjacency matrix with zeroes
        # the size of the matrix will be the largest node value
        max_value = self.get_max_node_value()+1
        adjacency_matrix = [[0]*max_value for i in range(max_value)]
        # now we traverse through the edges
        # and put the values in their correct position
        # the rows represent node_from values
        # the columns represent node_to values
        # the corresponding values are weights of edges
        for edge in self.edges:
            node_from_val = edge.node_from.value
            node_to_val = edge.node_to.value
            weight = edge.weight
            adjacency_matrix[node_from_val][node_to_val] = weight

        return adjacency_matrix

    def get_max_node_value(self):
        '''returns the maximum node_from value'''

        # we append all the node_from and node_to values into a list
        # and then return the max value of the list
        value_list=[]
        for node in self.nodes:
            value_list.append(node.value)
        return max(value_list)

# let's set the graph
graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)

# let's print the edges
# Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
print(graph.get_edge_list())

# Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
print(graph.get_adjacency_list())

# Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
print(graph.get_adjacency_matrix())
