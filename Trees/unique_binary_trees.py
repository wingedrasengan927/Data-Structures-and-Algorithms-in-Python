'''
Given an input n as the integer, you are required to find out all the combinations of the 
Binary Search Tree with nodes (1, n)

Example
-----------
Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]

Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

Solution
---------
1. Note that this is a binary search tree, each node in the left subtree must be less than the root
    and each node in the right subtree must be greater than the node
2. Let F(arr) be a function that takes in a list of *sorted nodes and returns all possible combinations
    of BSTs using that list
3. we iterate through the sorted input array, and consider the current element as root, Then we calculate 
    the number of combinations for left subarray F(left_arr) and number of combinations
    of right subarray F(right_arr)
4. Now with current element as the root, and different combinations of left subtree and right subtree, 
    we build different unique BSTs and return 
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []
        arr = list(range(1, n+1))
        return self.helper(arr)
        
    def helper(self, arr):
        if len(arr) == 0:
            return [None]
        combinations = []
        for i in range(len(arr)):
            leftSubtreeCombinations, rightSubtreeCombinations = self.helper(arr[:i]), self.helper(arr[i+1:])
            
            for leftSubtree in leftSubtreeCombinations:
                for rightSubtree in rightSubtreeCombinations:
                    root = TreeNode(arr[i])
                    root.left = leftSubtree
                    root.right = rightSubtree
                    combinations.append(root)
        
        return combinations
        