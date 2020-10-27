import random

def partition(arr, start_index, end_index):
    '''
    Partitioning
    --------------
    1. Pick an element (called pivot)
    2. manipulate the array such that
    3. left elements to the pivot are lesser than pivot
    4. right elements to pivot are greater than pivot
    '''

    pivot_element = arr[end_index]
    partition_index = start_index

    while start_index < end_index:
        if arr[start_index] <= pivot_element:
            arr[start_index], arr[partition_index] = arr[partition_index], arr[start_index]
            partition_index += 1
        start_index += 1

    arr[partition_index], arr[end_index] = arr[end_index], arr[partition_index]

    return partition_index


def quick_sort_helper(arr, start_index, end_index):
    if start_index >= end_index:
        return

    partion_index = partition(arr, start_index, end_index)

    quick_sort_helper(arr, start_index, partion_index-1)
    quick_sort_helper(arr, partion_index + 1, end_index)

    return arr

def quick_sort(arr):
    start_index = 0
    end_index = len(arr) - 1
    return quick_sort_helper(arr, start_index, end_index)
        
for k in range(10):
    random_array = [random.randrange(100) for i in range(10)]
    print("Array Before Sorting: {}".format(random_array))
    sorted_array = quick_sort(random_array)
    print("Array After Sorting: {}".format(sorted_array))
    print("-----------------------")