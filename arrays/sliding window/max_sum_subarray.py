'''
Kadanes Algorithm
'''

def max_sum_subarray(arr):
    current_sum = arr[0]
    max_sum = arr[0]
    for i in range(1, len(arr)):
        current_sum = max(current_sum + arr[i], arr[i])
        max_sum = max(current_sum, max_sum)
        
    return max_sum

arr = [-2, 2, 5, -11, 6]
print(max_sum_subarray(arr))