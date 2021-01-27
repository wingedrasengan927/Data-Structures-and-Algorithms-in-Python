'''
problem: https://www.techiedelight.com/0-1-knapsack-problem/
'''

def knapsack_01(values, weights, capacity):
    n = len(values)-1
    memo = dict()
    return helper_dp(values, weights, capacity, n, memo)

def helper_dp(values, weights, capacity, n, memo):
    # base case
    # the capacity is negative
    # -inf because we do not want to consider the item that leads to such value
    if capacity < 0:
        return float('-inf')

    # if n_items = 0 or capacity == 0
    if n < 0 or capacity == 0:
        return 0

    # memoization
    if (capacity, n) in memo:
        return memo[(capacity, n)]

    # we have two choices: either include the item or exclude it
    include = helper_dp(values, weights, capacity - weights[n], n-1, memo) + values[n]
    exclude = helper_dp(values, weights, capacity, n-1, memo)

    memo[(capacity, n)] = max(include, exclude)
    return memo[(capacity, n)]

# Input: set of items each with a weight and a value
v = [20, 5, 10, 40, 15, 25]
w = [1, 2, 3, 8, 7, 4]

# Knapsack capacity
W = 10

print(knapsack_01(v, w, W))