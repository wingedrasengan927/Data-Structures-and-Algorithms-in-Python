'''
max subarray sum where no two consecutive elements are included (no two adjacent elements)
'''

def max_sum_II(arr):
    '''
    1. This is a DP problem
    2. table[i] represents the max sum for the subarray arr[:i]
    3. at each point i, we can choose to keep the element i or not
    4. if we choose to keep element i, we have to add to it dp(i-2) (max sum upto i-2 elements)
        because we cannot add dp(i-1) since no two consecutive elements can be selected
    5. if we choose not to keep it, then we continue with the previous max sum of i-1 elements
    '''
    n = len(arr)
    table = [None] * n
    table[0] = arr[0]
    table[1] = max(arr[0], arr[1])
    for i in range(2, n):
        table[i] = max(arr[i] + table[i-2], table[i-1])
    return table[n-1]

arr = [-2, 1, -3, 4,-1, 2, 1, -5, 4]
print(max_sum_II(arr))