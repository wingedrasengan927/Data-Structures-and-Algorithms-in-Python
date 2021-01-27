'''
Question from Narasimha Karumahanchi's book
'''

cummulative_sum_array = []
def preprocess_cummulative_sum(arr):
    '''
    Here, the starting index should be exclusive, hence we add that extra element to cummulative_sum_array
    '''
    global cummulative_sum_array
    cummulative_sum_array.append(arr[0])
    for i in range(len(arr)):
        cummulative_sum_array.append(arr[i] + cummulative_sum_array[i])

def range_sum_query(i, j):
    return cummulative_sum_array[j+1] - cummulative_sum_array[i]

arr = [-2, 1, 6, -5, 9, -1, 19]

preprocess_cummulative_sum(arr)
print(range_sum_query(0, 1))