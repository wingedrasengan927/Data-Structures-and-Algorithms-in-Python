'''
Kadane's Algorithm or Largest subarray sum
'''

def max_continguos_sum(arr):
    '''
    1. We cannot use sliding window here as there is no condition for the window size
    2. This is a DP problem
    3. table[i] represents the max sum for the subarray arr[:i]
    4. at each point i, we can start afresh (consider only that element)
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