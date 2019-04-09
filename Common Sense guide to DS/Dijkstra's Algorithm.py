
# Observation:
# generally, while using 'or,' None should come first. Like, x = None or [] (x=[] in this case)

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
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes or []
        self.edges = edges or []
        self._node_map = {}
        self.node_names = []

    def insert_node(self, node_val):
        '''inserts a new node'''

        new_node = Node(node_val)
        self.nodes.append(new_node)
        self._node_map[node_val] = new_node
        return new_node

    def insert_edge(self, weight, node_from_val, node_to_val):
        '''inserts a new edge, creating new nodes if necessary'''

        nodes = {node_from_val: None, node_to_val:None}
        for node in self.nodes:
            if node.value in nodes:
                nodes[node.value] = node
                if all(nodes.values()):
                    break

        for node_val in nodes:
            nodes[node_val] = nodes[node_val] or self.insert_node(node_val)

        node_from = nodes[node_from_val]
        node_to = nodes[node_to_val]
        edge = Edge(weight, node_from, node_to)
        self.edges.append(edge)
        node_from.edges.append(edge)
        node_to.edges.append(edge)

    def set_node_names(self, names):
        """The Nth name in names should correspond to node number N.
        Node numbers are 0 based (starting at 0).
        """
        self.node_names = list(names)

    def get_edge_list(self):
        '''returns a list of tuples with format
        (weight, node_from_val, node_to_val)'''

        return [(edge.weight, edge.node_from.value, edge.node_to.value) for edge in self.edges]

    def get_edge_names(self):
        '''returns an edge list, except now the node values are translated to names'''

        return [(edge[0], self.node_names[edge[1]], self.node_names[edge[2]])
                for edge in self.get_edge_list()]

    def shortest_path(self, start_node_val, stop_node_val):
        '''returns the shortest path between two nodes'''

        # we initialise a list which will contain the shortest distances from the start node to every other node.
        # the length of this will be equal to the number of nodes present
        distance_list = [None] * len(self.node_names)
        # it's start_node value will be 0
        distance_list[start_node_val] = 0

        return self.dijkstras_algorithm(start_node_val, distance_list)[stop_node_val]

    def dijkstras_algorithm(self, current_node_val, distance_queue):
        '''helper for the shortest path function'''

        current_node = self._node_map[current_node_val]
        # we mark the current node as visited
        current_node.visited = True

        # We Now check all adjacent vertices and record the weights from the current vertex
        if current_node.visited is True:
            for edge in current_node.edges:
                if edge.node_to.visited is False:
                    # it is to be noted that the distance list contains only the shortest known routes
                    # so we update it only if the new distance is less than the current distance
                    if distance_queue[edge.node_to.value] is None or distance_queue[edge.node_to.value]>(distance_queue[current_node_val] + edge.weight):
                        distance_queue[edge.node_to.value] = distance_queue[current_node_val] + edge.weight


        # To determine the next current vertex, we find the cheapest unvisited known vertex that can be reached from our starting vertex.

        next_node_val = None
        next_node = None

        count = 0
        min = 10000000 # a very large value
        for i in distance_queue:
            node = self._node_map[count]
            if i is not None and node.visited is False:
                if i < min:
                    min = i
                    next_node_val = count
                    next_node = node
            count+=1

        # Repeat until we have visited every vertex in the graph.
        if next_node is not None:
            return self.dijkstras_algorithm(next_node_val, distance_queue)

        return distance_queue



# setting up the graph
# care should be maintained that the node values start from 0

graph = Graph()

graph.set_node_names(["Atlanta", # 0
                      "Boston", # 1
                      "Chicago", # 2
                      "Denver", # 3
                      "El Paso"]) # 4

# setting up the edges
graph.insert_edge(100, 0, 1)
graph.insert_edge(160, 0, 3)
graph.insert_edge(120, 1, 2)
graph.insert_edge(180, 1, 3)
graph.insert_edge(80, 2, 4)
graph.insert_edge(40, 3, 2)
graph.insert_edge(140, 3, 4)

# let's test the algorithm
print(graph.shortest_path(1, 4)) # it works!






