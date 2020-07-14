def intersection(nums1, nums2):
    '''
    Constant Space Solution
    '''
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    i = 0
    j = 0
    result = set()
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.add(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return list(result)