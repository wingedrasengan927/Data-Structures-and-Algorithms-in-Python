def max_continguos_sum_II(arr):
    n = len(arr)
    result = [0]*n
    result[0] = arr[0]
    result[1] = max(arr[0], arr[1])
    for i in range(2, n):
        result[i] = max(arr[i] + result[i-2], result[i-1], arr[i])
    return result[n-1]

arr = [-2, 1, -3, 4,-1, 2, 1, -5, 4]
print(max_continguos_sum_II(arr))