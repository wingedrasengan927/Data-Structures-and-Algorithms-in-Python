'''
find smallest subarray >= x
'''

def smallest_subarray(arr, target):
    '''
    The idea is to increase the size of the sliding window
    until we reach the desired criterion which is sum(subarray) >= x
    Once the reach the criterion, we decrease the size of the window
    and test the condition again so that we get the minimum size
    '''
    j = 0
    minSize = float('inf')
    for i in range(len(arr)):
        subarray = arr[j:i]
        # assuming that each element in the array is less than target
        while sum(subarray) >= target and j < i:
            size = i - j
            if size < minSize:
                minSize = size
            j += 1
            subarray = arr[j:i]

    return minSize

arr = [4, 2, 2, 7, 1, 8, 2, 1, 0]
print(smallest_subarray(arr, 8))