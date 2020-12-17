'''
Explanation: https://leetcode.com/problems/is-graph-bipartite/discuss/115493/Python-7-lines-DFS-graph-coloring-w-graph-and-Explanation
Problem: https://leetcode.com/problems/is-graph-bipartite/
'''
from collections import deque

class Solution:
    def isBipartite(self, graph):
        visited = {}
        for i in range(len(graph)):
            if i in visited:
                continue
            # can do with BFS or DFS
            if self.DFS(i, graph, visited, 1) == False:
                return False
        return True
        
        
    def DFS(self, i, graph, visited, current_color):
        if i in visited:
            if visited[i] != current_color:
                return False
            return True
        visited[i] = current_color
        neighbours = graph[i]
        for j in neighbours:
            if self.DFS(j, graph, visited, -current_color) == False:
                return False
        return True

    def BFS(self, i, graph, visited):
        queue = deque()
        start_node = (i, 1)
        queue.append(start_node)
        while len(queue) > 0:
            node, color = queue.popleft()
            if node in visited:
                if visited[node] != color:
                    return False
                continue
            visited[node] = color
            neighbours = graph[node]
            for v in neighbours:
                queue.append((v, -color))
        return True