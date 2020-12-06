'''
Kadane's Algorithm
'''

def max_continguos_sum(arr):
    '''
    1. This is a DP problem
    2. table[i] represents the max sum for the subarray arr[:i]
    3. at each point i, we can start afresh (consider only that element)
     or continue adding the previous max sum to the element
    '''
    n = len(arr)
    table = [None]*n
    table[0] = arr[0]
    for i in range(1, n):
        table[i] = max(table[i-1] + arr[i], arr[i])

    return table[n-1]

arr = [2, -6, 3, -2, 4, 1]
print(max_continguos_sum(arr))