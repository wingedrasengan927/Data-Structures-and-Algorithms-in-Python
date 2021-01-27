# reference: https://www.geeksforgeeks.org/python-program-for-matrix-chain-multiplication-dp-8/

'''
Question: Given an array p[] which represents the chain of matrices such that the ith matrix Ai is of 
dimension p[i-1] x p[i]. We need to write a function MatrixChainOrder() that should return the minimum number 
of multiplications needed to multiply the chain.

Input: p[] = {40, 20, 30, 10, 30}   
There are 4 matrices of dimensions 40x20, 20x30, 30x10 and 10x30.
'''
def main(p):
    # we have construct a list of matrices dimensions based on the list
    matrices_list = [[p[x-1], p[x]] for x in range(1, len(p))]
    memo = {}
    return DP(0, len(matrices_list), memo, matrices_list)

def DP(i, j, memo, p):
    '''
    Note that i, j represent the index of matrices.
    *j is exclusive
    '''
    if (i, j) in memo:
        return memo[(i, j)]

    if j - i == 1:
        memo[(i, j)] = 0
        return 0

    minCost = float('inf')
    for k in range(i+1, j):
        current_cost = DP(i, k, memo, p) + DP(k, j, memo, p) + (p[i][0] * p[k-1][1] * p[j-1][1])
        '''
        a note on cost - p[i][0] * p[k][0] * p[j-1][1]
        --------------------------------------
        - this is basically the cost that will incur if the parenthesis are placed at kth position
        - if we place parenthesis at kth position, we have to multiply matrices \
          (A_i, A_i+1, A_i+2....A_k-1) * (A_k, A_k+1, A_k+2, .....A_j)
        - Dimension of matrix 1: p[i]
        - Dimension of matrix 2: p[k-1]
        - Hence the cost is p[i][0] * p[k][0] * p[j-1][1]
        '''
        if current_cost < minCost:
            minCost = current_cost
            
    memo[(i,j)] = minCost
    return minCost

print(main([40, 20, 30, 10, 30]))


'''
--------------- Version 2 -------------
'''

def optimal_matrix_multiplication(p):
    list_of_matrices = [[p[x-1], p[x]] for x in range(1, len(p))]
    memo = dict()
    return dp(0, len(list_of_matrices), list_of_matrices, memo)

def dp(i, j, list_of_matrices, memo):
    # note that j is exclusive here
    if j - i <= 1: # base case: we have only one matrix
        return 0
    if (i, j) in memo:
        return memo[(i, j)]
    min_multiplications = float('inf')
    for k in range(i+1, j):
        # the cost of multiplying two matrices of shape m x k and k x n is m * k * n
        # here in multiplication, list_of_matrices[k][0] can be replaced with list_of_matrices[k-1][1]
        n_multiplications = dp(i, k, list_of_matrices, memo) + dp(k, j, list_of_matrices, memo) + \
             list_of_matrices[i][0] * list_of_matrices[k][0] * list_of_matrices[j-1][1]
        if n_multiplications < min_multiplications:
            min_multiplications = n_multiplications
    memo[(i, j)] = min_multiplications
    return memo[(i, j)]

print(optimal_matrix_multiplication([40, 20, 30, 10, 30]))