class ShortestPathResult:
    def __init__(self):
        self.parent = {}
        self.distance = {}

def shortest_path(graph, s):
    '''
    Find Shortest path from s to all the vertices in the graph using dynamic programming
    Args:
        graph: 2D List
            Weighted DAG
        s: 1D List
            vertex
    '''
    result =  ShortestPathResult()
    result.distance[s] = 0 # base case
    result.parent[s] = None
    for v in graph.itervertices():
        shortest_path_dp(graph, v, result)
    return result

def shortest_path_dp(graph, v, result):
    '''
    Find the Shortest Path to vertex v recursively using dynamic programming
    Args:
        graph: 2D List
            A Weighted DAG
        v: 1D list
            vertex to find the distance
        result:
            result object used for memoization of distance and parent
    '''
    if v in result.distance: # memoization
        return result.distance[v]
    result.distance[v] = float('inf')
    result.parent[v] = None
    for u in graph.inverse_vertices(v):
        current_distance = shortest_path_dp(graph, u, result) + graph.weight(u, v)
        if current_distance < result.distance[v]:
            result.distance[v] = current_distance
            result.parent[v] = u
    return result.distance[v]
    