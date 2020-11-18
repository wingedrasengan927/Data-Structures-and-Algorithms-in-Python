'''
Problem Statement and Explanation: Narasimha Karumanchi's Algorithm Design Patterns
'''

def n_choose_k(n, k):
    memo = dict()
    return dp(n, k, memo)

def dp(n, k, memo):
    if k==0 or n==k:
        return 1
    if (n, k) in memo:
        return memo[(n, k)]
    memo[(n, k)] = dp(n-1, k, memo) + dp(n-1, k-1, memo)
    return memo[(n, k)]

print(n_choose_k(5, 2))