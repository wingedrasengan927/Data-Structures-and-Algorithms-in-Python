'''
Problem: https://leetcode.com/explore/learn/card/binary-search/126/template-ii/947/
'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

def isBadVersion(num):
    return bool(num)

class Solution:
    def firstBadVersion(self, n):
        '''
        The idea behind template II is not to explicitly find the answer
        but to reduce the search space until we get the answer.
        So whenever you encounter template II problems, focus on how you can
        reduce the search space because generally in such type of questions,
        there'll always be an answer.
        In template two, our main focus is on the right neighbour
        The start element after reducing the search space is the required answer
        e.g., peak finding, minimum finding
        '''
        left = 0
        right = n
        while left < right:
            middle = (left + right) // 2
            if isBadVersion(middle):
                right = middle
            else:
                left = middle + 1
        return left

    '''
    A different kind of recursive soln based on finding the peak element
    '''
    def firstBadVersionv2(self, n):
        """
        Our objective in template two is to reduce the search space to it's extreme 
        and not find the answer right away
        """
        start = 1
        end = n
        if start == end:
            return start
        if isBadVersion(start):
            return start
        return self.helper(n, start, end)
        
        
    def helper(self, n, start, end):
        '''
        There are three options:
        1. Either mid + 1 is the first bad version
        2. first bad version lies in left search space or
        3. first bad version lies in right search space
        '''
        if start > end:
            return start
        mid = (start + end) // 2
        if mid + 1 <= n and isBadVersion(mid+1) and not (isBadVersion(mid)):
            return mid+1
        if mid+1 <= n and isBadVersion(mid+1):
            return self.helper(n, start, mid)
        if not isBadVersion(mid):
            return self.helper(n, mid+1, end)
        