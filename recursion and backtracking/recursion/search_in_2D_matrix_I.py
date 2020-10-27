'''
Search for a given target in a sorted 2D matrix

0 1 2 3 4
5 6 7 8 9
10 11 12 13 15
'''


def get_coordinate(index, n_cols):
    rowIdx = index // n_cols
    colIdx = index % n_cols
    return rowIdx, colIdx

def binarySearchHelper(matrix, target, startIdx, endIdx, n_cols):
    if startIdx > endIdx:
        return None
    midIdx = (startIdx + endIdx) // 2
    rowIdx, colIdx = get_coordinate(midIdx, n_cols)
    element = matrix[rowIdx][colIdx]
    if element > target:
        return binarySearchHelper(matrix, target, startIdx, midIdx-1, n_cols)
    elif element < target:
        return binarySearchHelper(matrix, target, midIdx+1, endIdx, n_cols)
    else:
        return (rowIdx, colIdx)

def binarySearch(matrix, target):
    '''
    Time Complexity - O(log(mn))
    '''
    n_cols = len(matrix[0])
    n_rows = len(matrix)
    startIdx = 0
    endIdx = n_cols*n_rows - 1
    return binarySearchHelper(matrix, target, startIdx, endIdx, n_cols)

matrix = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
print(binarySearch(matrix, 6))