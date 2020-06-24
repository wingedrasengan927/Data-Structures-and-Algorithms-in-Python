'''
find smallest subarray >= x
'''

def smallest_subarray(arr, target):
    j = 0
    minSize = float('inf')
    for i in range(len(arr)):
        subarray = arr[j:i]
        while sum(subarray) >= target and j < i:
            size = i - j
            if size < minSize:
                minSize = size
            j += 1
            subarray = arr[j:i]

    return minSize

arr = [4, 2, 2, 7, 1, 8, 2, 1, 0]
print(smallest_subarray(arr, 8))


