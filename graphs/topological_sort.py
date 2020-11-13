'''
Description and Algorithm here: https://www.interviewcake.com/concept/python3/topological-sort
'''

graph = {1: [2, 3], 2: [4, 5], 3: [4], 4: [5], 5: [None]}

def topological_sort(graph):
    # construct a dictionary mapping nodes to their indegrees
    indegrees = {node:0 for node in graph}
    for node in graph:
        for neighbour in graph[node]:
            indegrees[neighbour] = indegrees.get(neighbour, 0) + 1
        
    # track nodes with no incoming edges
    nodes_with_no_incoming_edges = []
    for node in indegrees:
        if indegrees.get(node) == 0:
            nodes_with_no_incoming_edges.append(node)

    topological_ordering = []

    # until we have exhausted all the nodes
    while len(nodes_with_no_incoming_edges) > 0:

        # add the nodes with no incoming edges to the topological ordering
        node = nodes_with_no_incoming_edges.pop()
        topological_ordering.append(node)

        # after adding the node to the topological ordering,
        # we remove the node and it's edges
        # to do so, we reduce the indegree of the node's neighbours by 1
        for neighbour in graph[node]:
            if neighbour == None:
                continue
            indegrees[neighbour] -= 1
            if indegrees[neighbour] == 0:
                nodes_with_no_incoming_edges.append(neighbour)

    return topological_ordering

print(topological_sort(graph))