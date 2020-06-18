'''
Given an array which is sorted and rotated, find a target, e.g., [4, 5, 0, 1, 2, 3]
'''

def binary_search_recursive(arr, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    # check if we've found the target
    if arr[mid] == target:
        return mid
    # check if mid lies in left sorted part
    if arr[start] <= arr[mid]: # left part is sorted
        # now lets check if the target lies in the left sorted part
        if arr[start] <= target < arr[mid]:
            return binary_search_recursive(arr, target, start, mid-1)
        else:
            return binary_search_recursive(arr, target, mid+1, end)
    # check if mid lies on the right sorted part
    elif arr[mid] <= arr[end]:
        # now check if target lies in the right sorted path
        if arr[mid] < target <= arr[end]:
            return binary_search_recursive(arr, target, mid+1, end)
        else:
            return binary_search_recursive(arr, target, start, mid-1)

arr = [6, 7, 8, 1, 2, 5]
target = 1
print(binary_search_recursive(arr, target, 0, len(arr)-1))