'''
Search in a 2D matrix
where rows are sorted and columns are sorted
but matrix is not sorted

1 4 7 11
8 9 10 20
11 12 17 30
'''

def search2DHelper(matrix, target, rowIdx, colIdx, n_cols):
    if rowIdx < 0 or colIdx >= n_cols:
        return None
    element = matrix[rowIdx][colIdx]
    if element > target:
        return search2DHelper(matrix, target, rowIdx-1, colIdx, n_cols)
    elif element < target:
        return search2DHelper(matrix, target, rowIdx, colIdx+1,n_cols)
    else:
        return (rowIdx, colIdx)

def search2D(matrix, target):
    '''
    Time Complexity - O(m + n)
    '''
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    rowIdx = n_rows - 1
    colIdx = 0
    return search2DHelper(matrix, target, rowIdx, colIdx, n_cols)

matrix = [[1, 4, 7, 11], [8, 9, 10, 20], [11, 12, 17, 30]]
target = 7
print(search2D(matrix, target))