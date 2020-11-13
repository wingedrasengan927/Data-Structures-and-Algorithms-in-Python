'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
'''

def combinations(n, k):
    result = []
    combinations_helper(n, k, 1, result, [])
    return result

def combinations_helper(n, k, index, result, combination):
    if len(combination) == k:
        result.append(combination)
        return
    for i in range(index, n+1):
        combinations_helper(n, k, i+1, result, combination + [i])

print(combinations(4, 2))