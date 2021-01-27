# reference: https://www.youtube.com/watch?v=DB-9JlnbBpM
# leetcode: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/submissions/

# drive code
def k_sum_partiton(nums, k):
    n = len(nums)
    if k > n:
        return False
    _sum = sum(nums)
    if _sum % k != 0:
        return False
    _sum = _sum // k
    target = [_sum] * k
    p = [[] for i in range(k)]
    partitions(k, nums, 0, target, p)
    return p
    # approach two
    visited = [False] * len(nums)
    return partitions2(0, k, nums, visited, 0, _sum)

def partitions(k, arr, i, target_arr, p):
    '''
    k - int
        No. of subsets
    arr - the original arr
    i - current index
    target_arr - the subset sum array
        length of this array would be - k
        each val in this array would be sum(arr) / k
    p - 2D array
        the output result containing partitions
    '''
    if i == len(arr):
        return sum(target_arr) == 0
    val = arr[i]
    for kx in range(k):
        if val <= target_arr[kx]:
            target_arr[kx] -= val
            if partitions(k, arr, i+1, target_arr, p):
                # store this value in the result
                p[kx].append(arr[i])
                # we put break statement here so as the same index could not be used in other partitions
                break
            else:
                # backtrack
                target_arr[kx] += val
    return sum(target_arr) == 0

# reference: https://www.youtube.com/watch?v=qpgqhp_9d1s

def partitions2(i, k, nums, visited,  current_k_sum, k_sum):
    '''
    base case:
    if we have one bucket left, it means we have successfully filled k-1 buckets and 
    that means we can also fill kth bucket as sum % k == 0
    '''
    if k == 1:
        return True
    if current_k_sum == k_sum:
        # we have successfully filled the kth bucket
        # let's move on to another bucket
        return partitions2(0, k-1, nums, visited, 0, k_sum)
    # fill the kth bucket
    for idx in range(i, len(nums)):
        if visited[idx] is True or nums[idx] + current_k_sum > k_sum:
            continue
        visited[idx] = True
        if partitions2(i+1, k, nums, visited, current_k_sum + nums[idx], k_sum) is True:
            return True
        visited[idx] = False
    return False

