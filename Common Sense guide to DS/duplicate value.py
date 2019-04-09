
# this function is used to check for duplicate values in linear time

def isDuplicate(array):
    # Let's initialize a very large empty array
    existingNumbers = [None]*10000
    '''So basically, we will iterate through the array once, and we will consider the values of input array
    as the indices of the existingNumbers array(hence we initialized a very large existingNumbers Array).
    Let's discuss through an example:
    Consider the array [4, 2, 7, 3, 4, 1]
    So initially, in the existingNumbers Array,
    the values in the indices: 4, 2, 7, 3 will be initialized as 1
    but when it encounters the value 4 again (after 7), since 4 is already filled with 7, it returns True
    There's only one for loop (Iterates through the array only once) and hence it's time complexity is O(N)
    '''
    for i in range(len(array)):
        if not existingNumbers[array[i]]:
            existingNumbers[array[i]]=1
        else:
            return True
    return False

print(isDuplicate([4, 2, 3]))
