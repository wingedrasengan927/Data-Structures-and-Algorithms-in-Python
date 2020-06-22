import random

def insertion_sort(arr):
    if len(arr) == 1:
        return arr
    for i in range(1, len(arr)):
        current_index = i
        for j in reversed(range(i)):
            if arr[current_index] < arr[j]:
                arr[current_index], arr[j] = arr[j], arr[current_index]
                current_index = j
    return arr

for k in range(10):
    random_array = [random.randrange(100) for i in range(10)]
    print("Array Before Sorting: {}".format(random_array))
    sorted_array = insertion_sort(random_array)
    print("Array After Sorting: {}".format(sorted_array))
    print("-----------------------")