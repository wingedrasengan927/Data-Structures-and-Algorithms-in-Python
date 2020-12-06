'''
Max sum where 3 consecutive elements cannot be included. (2 consecutive elements can)
'''

def max_sum_III(arr):
    n = len(arr)
    table = [None]*n
    table[0] = arr[0]
    table[1] = max(table[0], arr[1]+arr[0])
    table[2] = max(table[1], arr[2]+table[0], arr[2] + arr[1])
    for i in range(3, n):
        table[i] = max(arr[i] + arr[i-1] + table[i-3], arr[i] + table[i-2], table[i-1])
    return table[n-1]

arr = [2, 13, 16, 100, 4, 5]
print(max_sum_III(arr))