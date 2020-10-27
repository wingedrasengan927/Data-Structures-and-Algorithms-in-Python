'''
Given a binary tree, find the number of topologies it can take

Solution
---------
1. Say F(n) is the number of binary tree topologies with n nodes
2. Say a tree has 5 nodes. If we fix the root, the number of binary tree topologies are:
3. F(0)*F(4) + F(1)*F(3) + F(2)*F(2) + F(3)*F(1) + F(4)*F(0) where the left function represents the 
   number of binary tree topologies for left subtree and the right function for right subtree
4. So essentially we iterate through 0 to n-1, and calculate F(i)*F(n-1-i) and sum it cummulatively
5. Also, we will need memoization here because we will be calculating the value of F(n) multiple times 
'''

def number_of_binary_tree_topologies(n):
   memo = dict()
   return number_of_binary_tree_topologies_helper(n, memo)

def number_of_binary_tree_topologies_helper(n, memo):
   if n == 0 or n == 1:
      return 1
   if n in memo:
      return n
   n_topologies = 0
   for i in range(n):
      n_topologies += number_of_binary_tree_topologies_helper(i, memo) * number_of_binary_tree_topologies_helper(n-1-i, memo)
   memo[n] = n_topologies
   return memo[n]

print(number_of_binary_tree_topologies(3))
   