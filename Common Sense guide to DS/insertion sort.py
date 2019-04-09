
def insertion_sort(array):
    for i in range(1, len(array)):
        temp_index = i
        temp_value = array[i]
        while temp_index>0 and array[temp_index-1]>temp_value:
            array[temp_index] = array[temp_index-1]
            temp_index = temp_index-1
        array[temp_index] = temp_value


arr1 = [4, 2, 7, 1, 3]
insertion_sort(arr1)
print(arr1)
arr2 = [3, 7, 1, 8, 9]
print(arr2)