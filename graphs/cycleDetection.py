'''
Problem: https://leetcode.com/problems/find-eventual-safe-states/submissions/
'''

class Solution:
    def eventualSafeNodes(self, graph):
        '''
        The idea is we iterate through each vertex and check if a backedge is present
        in that vertex. We use a recursion Stack to reset after we move to the next vertex.
        '''
        visited = [False]*len(graph)
        recStack = [False]*len(graph)
        result = []
        n= len(graph)
        for v in range(n):
            if not self.isCycle(v, graph, visited, recStack):
                result.append(v)
        return result
        
    def isCycle(self, v, graph, visited, recStack):
        '''
        There is a cycle if the vertex has been visited previously
        and is also in the recursion stack  
        '''
        visited[v] = True
        recStack[v] = True
        neighbours = graph[v]
        for u in neighbours:
            if visited[u] == False:
                if self.isCycle(u, graph, visited, recStack):
                    return True
            elif recStack[u] == True:
                return True
        recStack[v] = False
        return False