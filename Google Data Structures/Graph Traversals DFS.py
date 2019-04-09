
class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False

class Edge:
    def __init__(self, weight, node_from, node_to):
        self.weight = weight
        self.node_from = node_from
        self.node_to = node_to

class Graph:

    def __init__(self):
        self.nodes = []
        self.edges = []

    def insert_node(self, value):
        new_node = Node(value)
        self.nodes.append(new_node)

    def insert_edge(self, value, node_from_val, node_to_val):
        node_from = None
        node_to = None
        for node in self.nodes:
            if node.value == node_from_val:
                node_from = node
            if node.value == node_to_val:
                node_to = node
        if node_from is None:
            node_from = Node(node_from_val)
            self.nodes.append(node_from)
        if node_to is None:
            node_to = Node(node_to_val)
            self.nodes.append(node_to)
        new_edge = Edge(value, node_from, node_to)
        self.edges.append(new_edge)
        node_from.edges.append(new_edge)
        node_to.edges.append(new_edge)

    def dfs(self, start_node_val):
        '''performs a depth first traversal'''

        # first, we search for the start node given the start value
        start_node = None
        for node in self.nodes:
            if start_node_val == node.value:
                start_node = node

        return self.dfs_helper(start_node, [])

    def dfs_helper(self, node, traversal):
        '''helper for the dfs function'''

        # let's demonstrate how this works
        # this is similar to the delete node function in binary search tree
        # the start node here is 1

        # function(1)
        #   print(1)
        #   1 --> visited
        #   function(2)
        #       print(2)
        #       2 --> visited
        #       # base case reached (since 2 has no unvisited nodes)
        #       # **we can return anything (even none) what's more important is the base case has been reached. not the return value**
        #       return
        #   # Now, function(1) continues where it has left
        #   # which was in the middle of the for loop. Now, it goes to the next edge
        #   function(3)
        #       print(3)
        #       3 --> visited
        #       function(4)
        #           print(4)
        #           4 --> visited
        #           # base case reached
        #           return
        #       # Now, function(3) continues where it has left
        #       # which was in the middle of the for loop.
        #       # it checks whether 3 has any unvisited nodes. It has none
        #       # base case reached
        #       return
        #   # Now, function(1) continues where it has left
        #   # which was in the middle of the for loop. Now, it checks if any unvisited nodes are there. It has none
        #   # base case reached
        #   return


        if node.visited is False:
            traversal.append(node.value)
            node.visited = True
        for edge in node.edges:
            if edge.node_to.visited is False:
                self.dfs_helper(edge.node_to, traversal)
        # we can return anything
        # what's more important is the base case has been reached. Not the return value
        return traversal



# let's set the graph
graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)

print(graph.dfs(1))
