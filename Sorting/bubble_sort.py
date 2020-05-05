# reference: https://realpython.com/sorting-algorithms-python/#the-bubble-sort-algorithm-in-python

import random

def bubble_sort(arr):
    flag = True
    n = len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j] > arr[j + 1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                flag = False
        if flag:
            break
    
    return arr

for k in range(10):
    random_array = [random.randrange(100) for i in range(10)]
    print("Array Before Sorting: {}".format(random_array))
    sorted_array = bubble_sort(random_array)
    print("Array After Sorting: {}".format(sorted_array))
    print("-----------------------")
