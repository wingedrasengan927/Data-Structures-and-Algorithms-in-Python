'''
Problem: https://leetcode.com/contest/weekly-contest-216/problems/minimum-initial-energy-to-finish-tasks/
'''

class Solution:
    def minimumEffort(self, tasks):
        # sort them based of diff
        tasks = sorted(tasks, key = lambda x: x[1]-x[0], reverse=True)
        total_cost = curr_cost = 0
        # curr cost is the residual cost we carry to the next task
        for cost, min_cost in tasks:
            if min_cost > curr_cost:
                total_cost += (min_cost-curr_cost)
                curr_cost = min_cost
            curr_cost -= cost
        return total_cost
                
        