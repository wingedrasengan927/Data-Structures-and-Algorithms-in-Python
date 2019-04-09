from collections import deque

# Note: if we're using an 'or' logical operator
#       if both values on the either side of the operator are true,
#       then the first one is returned
#       for example: return 3 or 4 returns 3


class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False


class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes or [] # if nothing is passed as an argument, an empty list is assigned to self.nodes
        self.edges = edges or []
        self.node_names = []
        self._node_map = {} # maps node values to nodes

    def insert_node(self, new_node_val):
        '''inserts a new node to the graph'''

        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        self._node_map[new_node_val] = new_node
        return new_node

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        "Insert a new edge, creating new nodes if necessary"

        # first we search if the node is present
        # if it is present, then we assign it to the nodes dictionary
        nodes = {node_from_val: None, node_to_val: None}
        for node in self.nodes:
            if node.value in nodes:
                nodes[node.value] = node
                if all(nodes.values()): # all() returns True if all of the values are True
                    break
        # if the node with the given value is not present,
        # then we create a new node using the insert_node() method and assign it to the nodes dictionary
        for node_val in nodes:
            nodes[node_val] = nodes[node_val] or self.insert_node(node_val)
        # finally, we create the new edge
        node_from = nodes[node_from_val]
        node_to = nodes[node_to_val]
        new_edge = Edge(new_edge_val, node_from, node_to)
        node_from.edges.append(new_edge)
        node_to.edges.append(new_edge)
        self.edges.append(new_edge)

    def set_node_names(self, names):
        """The Nth name in names should correspond to node number N.
        Node numbers are 0 based (starting at 0).
        """
        self.node_names = list(names)

    def get_edge_list(self):
        """Return a list of triplets that looks like this:
        (Edge Value, From Node, To Node)"""
        return [(edge.value, edge.node_from.value, edge.node_to.value) for edge in self.edges]

    def get_edge_list_names(self):
        """Return a list of triples that looks like this:
        (Edge Value, From Node Name, To Node Name)"""
        return [(edge[0], self.node_names[edge[1]], self.node_names[edge[2]])
                for edge in self.get_edge_list()]

    def get_adjacency_list(self):
        """Return a list of lists.
        The indices of the outer list represent "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""

        length = self.get_max_node() # here, no need to add +1 because get_max_node returns the number of nodes directly
        adjacency_list = [None]*length
        for edge in self.get_edge_list():
            if adjacency_list[edge[1]] is None:
                adjacency_list[edge[1]] = [(edge[2], edge[0])]
            else:
                adjacency_list[edge[1]].append((edge[2], edge[0]))
        return adjacency_list

    def get_adjacency_list_names(self):
        """Each section in the list will store a list
        of tuples that looks like this:
        (To Node Name, Edge Value).
        Node names should come from the names set
        with set_node_names."""

        length = self.get_max_node()
        adjacency_list_names = [None]*length
        for edge in self.get_edge_list_names():
            node_index = self.node_names.index(edge[1])
            if adjacency_list_names[node_index] is None:
                adjacency_list_names[node_index] = [(edge[2], edge[0])]
            else:
                adjacency_list_names[node_index].append((edge[2], edge[0]))
        return adjacency_list_names


    def get_max_node(self):
        """Return the highest found node number
        Or the length of the node names if set with set_node_names()."""

        if len(self.node_names) > 0:
            return len(self.node_names)
        else:
            return max(self._node_map.keys())

    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""

        length = self.get_max_node()
        adjacency_matrix = [[0]*length for i in range(length)]
        for edge in self.get_edge_list():
            adjacency_matrix[edge[1]][edge[2]] = edge[0]
        return adjacency_matrix

    def find_node(self, node_number):
        "Return the node with value node_number or None"
        return self._node_map.get(node_number)

    def _clear_visited(self):
        for node in self.nodes:
            node.visited = False

    # this is the solution provided by google
    # however, my solution works just fine

    def dfs_helper(self, start_node):
        """The helper function for a recursive implementation
        of Depth First Search iterating through a node's edges. The
        output should be a list of numbers corresponding to the
        values of the traversed nodes.
        ARGUMENTS: start_node is the starting Node
        REQUIRES: self._clear_visited() to be called before
        MODIFIES: the value of the visited property of nodes in self.nodes
        RETURN: a list of the traversed node values (integers).
        """
        ret_list = [start_node.value]
        start_node.visited = True
        edges_out = [e for e in start_node.edges
                     if e.node_to.value != start_node.value]
        for edge in edges_out:
            if not edge.node_to.visited:
                ret_list.extend(self.dfs_helper(edge.node_to))
        return ret_list


    def dfs(self, start_node_num):
        """Outputs a list of numbers corresponding to the traversed nodes
        in a Depth First Search.
        ARGUMENTS: start_node_num is the starting node number (integer)
        MODIFIES: the value of the visited property of nodes in self.nodes
        RETURN: a list of the node values (integers)."""
        self._clear_visited()
        start_node = self.find_node(start_node_num)
        return self.dfs_helper(start_node)


    def dfs_names(self, start_node_num):
        """Return the results of dfs with numbers converted to names."""
        return [self.node_names[num] for num in self.dfs(start_node_num)]

    # this is the solution provided by google
    # however, my solution works just fine

    def bfs(self, start_node_num):
        """An iterative implementation of Breadth First Search
        iterating through a node's edges. The output should be a list of
        numbers corresponding to the traversed nodes.
        ARGUMENTS: start_node_num is the node number (integer)
        MODIFIES: the value of the visited property of nodes in self.nodes
        RETURN: a list of the node values (integers)."""
        node = self.find_node(start_node_num)
        self._clear_visited()
        ret_list = []
        queue = [node]
        node.visited = True
        def enqueue(n, q=queue):
            n.visited = True
            q.append(n)
        def unvisited_outgoing_edge(n, e):
            return ((e.node_from.value == n.value) and
                    (not e.node_to.visited))
        while queue:
            node = queue.pop(0)
            ret_list.append(node.value)
            for e in node.edges:
                if unvisited_outgoing_edge(node, e):
                    enqueue(e.node_to)
        return ret_list

    def bfs_names(self, start_node_num):
        """Return the results of bfs with numbers converted to names."""
        return [self.node_names[num] for num in self.bfs(start_node_num)]


# setting up the graph
# we set up in such a way that each node corresponds to a city
graph = Graph()

graph.set_node_names(('Mountain View',  # 0
                      'San Francisco',  # 1
                      'London',  # 2
                      'Shanghai',  # 3
                      'Berlin',  # 4
                      'Sao Paolo',  # 5
                      'Bangalore'))  # 6

graph.insert_edge(51, 0, 1)  # MV <-> SF
graph.insert_edge(51, 1, 0)  # SF <-> MV
graph.insert_edge(9950, 0, 3)  # MV <-> Shanghai
graph.insert_edge(9950, 3, 0)  # Shanghai <-> MV
graph.insert_edge(10375, 0, 5)  # MV <-> Sao Paolo
graph.insert_edge(10375, 5, 0)  # Sao Paolo <-> MV
graph.insert_edge(9900, 1, 3)  # SF <-> Shanghai
graph.insert_edge(9900, 3, 1)  # Shanghai <-> SF
graph.insert_edge(9130, 1, 4)  # SF <-> Berlin
graph.insert_edge(9130, 4, 1)  # Berlin <-> SF
graph.insert_edge(9217, 2, 3)  # London <-> Shanghai
graph.insert_edge(9217, 3, 2)  # Shanghai <-> London
graph.insert_edge(932, 2, 4)  # London <-> Berlin
graph.insert_edge(932, 4, 2)  # Berlin <-> London
graph.insert_edge(9471, 2, 5)  # London <-> Sao Paolo
graph.insert_edge(9471, 5, 2)  # Sao Paolo <-> London
# (6) 'Bangalore' is intentionally disconnected (no edges)
# for this problem and should produce None in the
# Adjacency List, etc.

# ['London', 'Shanghai', 'Berlin', 'Sao Paolo', 'Mountain View', 'San Francisco']
print(graph.bfs_names(2))