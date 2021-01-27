'''
find longest substring length with k distinct characters
'''

def longest_substring(arr, k):
    '''
    The idea is to prepare a hash map with char - count mapping
    and update the hashmap as we move along the array.
    when the condition is met i.e number of distinct characters is equal to k
    when calculate and update the min size 
    if the number of distinct characters are more than k,
    we decrease the size of the sliding window until the condition is satisfied
    '''
    hash_map = {}
    j = 0
    result = -float('inf')
    for i in range(len(arr)):
        hash_map[arr[i]] = hash_map[arr[i]] + 1 if arr[i] in hash_map else 1
        while len(hash_map) > k:
            # remove items with zero in it - because we are checking the len of hashmap as condition
            for key, val in hash_map.items():
                if val == 0:
                    hash_map.pop(key)
            hash_map[arr[j]] -= 1
            j += 1
        else:
            if len(hash_map) == k:
                size = sum(hash_map.values())
                if size > result:
                    result = size
    return result
 
arr = ["a", "a", "a", "h", "h", "i", "b", "c"]
print(longest_substring(arr, 2))