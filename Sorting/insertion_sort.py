import random

def insertion_sort(arr):
    for i in range(1, len(arr)):

        current_value = arr[i]
        prev_index = i - 1

        while prev_index >= 0 and arr[prev_index] > current_value:
            arr[prev_index + 1] = arr[prev_index]
            prev_index -= 1

        arr[prev_index + 1] = current_value

    return arr

for k in range(10):
    random_array = [random.randrange(100) for i in range(10)]
    print("Array Before Sorting: {}".format(random_array))
    sorted_array = insertion_sort(random_array)
    print("Array After Sorting: {}".format(sorted_array))
    print("-----------------------")