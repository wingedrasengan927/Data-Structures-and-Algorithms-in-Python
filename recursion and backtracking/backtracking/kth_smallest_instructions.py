'''
Question: https://leetcode.com/problems/kth-smallest-instructions/
'''

class Solution:
    def kthSmallestPath(self, destination, k):
        result = []
        maxRow = destination[0]
        maxColumn = destination[1]
        self.globalCount = 0
        return self.kthSmallestPathHelper(destination, "", 0, 0, maxRow, maxColumn, result, k)
        
    def kthSmallestPathHelper(self, destination, currentPath, currentRow, currentColumn, maxRow, maxColumn, result, k):
        if currentRow == destination[0] and currentColumn == destination[1]:
            self.globalCount += 1
            # print(currentPath, self.globalCount)
            if self.globalCount == k:
                return currentPath
            else:
                return None
        if currentRow > maxRow:
            return None
        if currentColumn > maxColumn:
            return None
        is_result_one = self.kthSmallestPathHelper(destination, currentPath + "H", currentRow, currentColumn+1, maxRow, maxColumn, result, k)
        is_result_two = self.kthSmallestPathHelper(destination, currentPath + "V", currentRow+1, currentColumn, maxRow, maxColumn, result, k)
        
        return is_result_one or is_result_two