class Solution:
    def getRow(self, rowIndex):
        i = rowIndex
        result = []
        memo = dict()
        for j in range(i+1):
            result.append(self.get_element(i, j, memo))
        return result
        
    def get_element(self, i, j, memo): # i - rowIndex, j - columnIned
        if i == 0 or j == 0 or i==j:
            return 1
        if (i, j) in memo:
            return memo[(i, j)]
        
        # F(i, j) = F(i-1, j-1) + F(i-1, j) # recurrence relation
        memo[(i, j)] = self.get_element(i-1, j-1, memo) + self.get_element(i-1, j, memo)
        return memo[(i, j)]