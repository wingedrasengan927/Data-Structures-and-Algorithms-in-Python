def binary_search(arr, target):
    i = 0
    j = len(arr)
    while i < j:
        middle_index = (i + j) // 2
        if arr[middle_index] == target:
            return middle_index
        elif arr[middle_index] < target:
            i = middle_index + 1
        else:
            j = middle_index - 1
    return False

def binary_search_recursion(arr, target, start, end):
    if start >= end:
        return False
    middle_index = (start + end) // 2
    if arr[middle_index] == target:
        return middle_index
    elif arr[middle_index] > target:
        return binary_search_recursion(arr, target, start, end-1)
    else:
        return binary_search_recursion(arr, target, start+1, end)

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10
print(binary_search(arr1, target))
print(binary_search_recursion(arr1, target, 0, len(arr1)))