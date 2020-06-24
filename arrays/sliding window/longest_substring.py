'''
find longest substring length with k distinct characters
'''

def longest_substring(arr, k):
    hash_map = {}
    j = 0
    result = -float('inf')
    for i in range(len(arr)):
        hash_map[arr[i]] = hash_map[arr[i]] + 1 if arr[i] in hash_map else 1
        while len(hash_map) > k:
            # remove items with zero in it
            for key, val in hash_map.items():
                if val == 0:
                    hash_map.pop(key)
            hash_map[arr[j]] -= 1
            j += 1
        else:
            size = sum(hash_map.values())
            if size > result:
                result = size
    return result
 
arr = ["a", "a", "a", "h", "h", "i", "b", "c"]
print(longest_substring(arr, 2))