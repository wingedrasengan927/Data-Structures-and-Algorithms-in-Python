def max_sum_subarray(arr, window_size):
    if window_size > arr:
        return sum(arr)
    j = 0
    max_sum = -float('inf')
    for i in range(window_size, len(arr)):
        _sum = sum(arr[j:i])
        if _sum > max_sum:
            max_sum = _sum
        j += 1
    return max_sum

arr = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
print(max_sum_subarray(arr, 3))