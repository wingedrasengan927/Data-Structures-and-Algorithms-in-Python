'''
Problem: https://leetcode.com/problems/subarrays-with-k-different-integers/submissions/
'''

class Solution:
    def subarraysWithKDistinct(self, A, K):
        '''
        This is basically saying, give me the amount of subarrays 
        we can form with at most K, and give me the amount of subarrays 
        we can form with at most K-1, and the diff between the two will be ONLY 
        subarrays at K (since we have eliminated everything K-1 and under).
        
        This is the trick used in atmostK sliding window problems
        '''
        return self.atMostK(A, K) - self.atMostK(A, K-1)
    
    def atMostK(self, A, K):
        j = 0
        hash_map = dict()
        result = 0
        for i, val in enumerate(A):
            if hash_map.get(val, 0) == 0:
                K -= 1
            hash_map[val] = hash_map[val] + 1 if val in hash_map else 1
            while K < 0 and j<=i:
                hash_map[A[j]] -= 1
                if hash_map[A[j]] == 0:
                    K += 1
                j += 1
            # Generally in problems they ask for the max length or min length of subarray
            # but here in this problem they are asking for the number of possibilities
            # coincidentally, the length of the subarray also gives us the number of possibilites
            # example: [1, 2, 1, 2] - length = 4, possibilities are [1, 2, 1], [2, 1, 2], [1, 2], [1, 2, 1, 2] which is 4
            # i-j+1 is the length of subarray with atmost K distinct elements
            result += i - j + 1 
        return result