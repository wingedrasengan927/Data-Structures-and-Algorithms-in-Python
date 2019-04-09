
# function which returns the intersection between two arrays

def intersection(array1, array2):
    itn = []
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i] == array2[j]:
                itn.append(array2[j])
                break
    return itn

arr1 = [1, 3, 5, 7, 34]
arr2 = [3, 1, 22, 23, 12]

print(intersection(arr1, arr2))
