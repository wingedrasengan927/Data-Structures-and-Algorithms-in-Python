def binary_search(arr, target):
    start = 0
    end = len(arr)
    while start < end:
        middle_index = (start + end) // 2
        if arr[middle_index] == target:
            return middle_index
        elif target > arr[middle_index]:
            start = middle_index + 1
        else:
            end = middle_index - 1
    return -1

def find_first(arr, target):
    '''
    Find the index of first element if the element has duplicates
    '''
    index = binary_search(arr, target)
    if index == -1:
        return False
    while index >= 0:
        if arr[index] != target:
            return index + 1
        index -= 1 
    return index + 1
    
def find_first_last(arr, target):
    '''
    find the start index and end index of the target if it has duplicates
    '''
    index = binary_search(arr, target)
    if index == -1:
        return False
    first_index = index
    while first_index >= 0:
        if arr[first_index] != target:
            break
        first_index -= 1
    first_index += 1
    last_index = index
    while last_index < len(arr):
        if arr[last_index] != target:
            break
        last_index += 1
    last_index -= 1
    return [first_index, last_index]
        


multiple = [1, 1, 3, 5, 7, 7, 7, 8, 11, 12, 12]
target = 1



print(find_first(multiple, target))
print(find_first_last(multiple, target))