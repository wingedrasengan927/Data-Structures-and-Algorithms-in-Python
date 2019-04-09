
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False

class Edge:
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph:
    def __init__(self):
        self.edges = []
        self.nodes = []


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

    def bfs(self, start_node_val):
        '''runs a breadth first search'''

        # search for the node given the node value
        start_node = None
        for node in self.nodes:
            if node.value == start_node_val:
                start_node = node

        # define an empty queue
        queue = deque([])

        return self.bfs_helper(start_node, [], queue)

    def bfs_helper(self, node, traversal, queue):
        '''helper for the bfs function'''

        # if a node is not visited, check it off and append it to the list
        if node.visited is False:
            traversal.append(node.value)
            node.visited = True

        # search if there are any unvisited nodes connected to this node
        # If so, check them off and append them to our traversal list
        # and also, add them to the queue
        for edge in node.edges:
            node_to = edge.node_to
            if node_to.visited is False:
                queue.append(node_to)
                traversal.append(node_to.value)
                node_to.visited = True
        # base case
        # if the queue is empty, we've searched all nodes and reached the base case
        if len(queue) == 0:
            return traversal
        # we pop up the elements from the queue and run the function on them
        return self.bfs_helper(queue.popleft(), traversal, queue)


# let's set the graph
graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)
graph.insert_edge(111, 3, 5)

print(graph.bfs(1))













