def swap(idx1, idx2, array):
    array[idx1], array[idx2] = array[idx2], array[idx1]

def partition(start_index, end_index, array):
    leftPointer = start_index + 1
    rightPointer = end_index
    pivotPointer = start_index
    while leftPointer <= rightPointer:
        if array[leftPointer] > array[pivotPointer] and array[rightPointer] < array[pivotPointer]:
            swap(leftPointer, rightPointer, array)
        elif array[leftPointer] <= array[pivotPointer]:
            leftPointer += 1
        elif array[rightPointer] >= array[pivotPointer]:
            rightPointer -= 1
    swap(rightPointer, pivotPointer, array)
    pivotPointer = rightPointer

    return pivotPointer

def quickselect_helper(array, start_index, end_index, k):
    partition_index = partition(start_index, end_index, array)
    if k > partition_index:
        return quickselect_helper(array, partition_index + 1, end_index, k)
    elif k < partition_index:
        return quickselect_helper(array, start_index, partition_index - 1, k)
    else:
        return array[partition_index]

def quickselect(array, k):
    '''
    Time Complexity - O(n)
    '''
    return quickselect_helper(array, 0, len(array)-1, k)

array = [8, 5, 2, 9, 7, 6, 3]
k = 2
print(quickselect(array, k))