'''
problem: https://leetcode.com/problems/time-needed-to-inform-all-employees/
'''

class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):
        '''
        This problem is very similar to 'get max path sum in a tree'
        '''
        # get manager-employee mapping
        employees = [[] for i in range(n)]
        for idx, m in enumerate(manager):
            if m == -1:
                continue
            employees[m].append(idx)
        return self.DFS(headID, employees, informTime)    
        
    def DFS(self, rootID, employees, informTime):
        return max([self.DFS(employeeID, employees, informTime) for employeeID in employees[rootID]] or [0]) + informTime[rootID]