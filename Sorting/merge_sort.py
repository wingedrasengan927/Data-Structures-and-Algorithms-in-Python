import random

def merge(left_array, right_array, main_array):
    i = 0 # left array counter
    j = 0 # right array counter
    k = 0 # main array counter

    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            main_array[k] = left_array[i]
            i += 1
        elif left_array[i] > right_array[j]:
            main_array[k] = right_array[j]
            j += 1
        k += 1

    while i < len(left_array):
        main_array[k] = left_array[i]
        i += 1
        k += 1
    
    while j < len(right_array):
        main_array[k] = right_array[j]
        j += 1
        k += 1

    return main_array

def merge_sort(arr):
    if len(arr) < 2:
        return
    
    mid = len(arr) // 2
    left_array = arr[:mid]
    right_array = arr[mid:]

    merge_sort(left_array)
    merge_sort(right_array)

    return merge(left_array, right_array, arr)
        
for k in range(10):
    random_array = [random.randrange(100) for i in range(10)]
    print("Array Before Sorting: {}".format(random_array))
    sorted_array = merge_sort(random_array)
    print("Array After Sorting: {}".format(sorted_array))
    print("-----------------------")