'''
1. First row Starts with 0
2. children of 0 are 0 and 1 in the order
3. children of 1 are 1 and 0 in the order
4. find Kth index of Nth row

example
---------
N=4, k=5
0
01
0110
01101001

ans: 5 (1 indexed)

Solution
---------
1. One observation is that if K is odd, then the node is left child of it's parent
2. Else if K is even, then the node is right child of it's parent
3. based on this, we find the parent recursively and return the node accordingly
'''
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N==1:
            return 0
        
        if K%2 == 0:
            if self.kthGrammar(N-1, K/2) == 0:
                return 1
            else:
                return 0
        else:
            if self.kthGrammar(N-1, (K+1)/2) == 0:
                return 0
            else:
                return 1