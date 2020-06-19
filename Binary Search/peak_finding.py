'''
Find Peak in 1D and 2D arrays using binary search
'''
import numpy as np

def find_peak_1D(arr, start, end):
    mid = (start + end) // 2
    if mid+1 < len(arr):
        if arr[mid] <= arr[mid+1]:
            return find_peak_1D(arr, mid+1, end)
    if mid-1 >= 0:
        if arr[mid] <= arr[mid-1]:
            return find_peak_1D(arr, start, mid-1)
    return mid

arr = [1, 2, 4, 5, 6, 3, 2, 1] 
print(find_peak_1D(arr, 0, len(arr)-1))

def find_peak_2D(matrix, start_col, end_col):
    j = (start_col + end_col) // 2
    i = np.argmax(matrix[:, j])
    if j + 1 < matrix.shape[1]:
        if matrix[i, j] <= matrix[i, j+1]:
            return find_peak_2D(matrix, j+1, end_col)
    if j - 1 >= 0:
        if matrix[i, j] < matrix[i, j-1]:
            return find_peak_2D(matrix, start_col, j-1)
    return matrix[i, j]

matrix = np.array([[11, 12, 13, 14], [5, 6, 8, 25], [17, 18, 19, 20]])
print(find_peak_2D(matrix, 0, matrix.shape[1]-1))