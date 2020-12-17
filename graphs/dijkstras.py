'''
Problem: https://leetcode.com/problems/network-delay-time/submissions/
'''

from graph_rep import Graph

def dijkstras(self, graph, source):
    visited = set()
    distance = [float('inf')] * graph.n_nodes
    vertices = list(range(graph.n_nodes))

    # initialize source
    distance[source] = 0

    while len(vertices) > 0:
        # get current node
        # the current node is the node which has minimum distance from the source
        min_distance = float('inf')
        min_node = None
        for node in vertices:
            if node in visited:
                continue
            if distance[node] < min_distance:
                min_distance = distance[node]
                min_node = node

        visited.add(min_node)
        vertices.remove(min_node)

        # perform relaxation on neighbours of the current node
        neighbours = graph.adj_list[min_node]
        for v in neighbours:
            edge_weight = graph.adj_matrix[min_node][v]
            current_distance = edge_weight + min_distance
            if current_distance < distance[v]:
                distance[v] = current_distance

    return distance