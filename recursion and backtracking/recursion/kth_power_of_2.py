'''
Given k, n find n^k
'''

memo = dict()
def kth_power_of_n(n, k):
    if k == 0:
        return 1
    if k == 1:
        return n
    if k < 0:
        k = abs(k) 
        n = 1/n  

    if (n, k) in memo:
        return memo[(n, k)]

    if k % 2 == 0:
        memo[(n, k)] = kth_power_of_n(n, k//2) * kth_power_of_n(n, k//2)
    else:
        memo[(n, k)] = kth_power_of_n(n, k//2)*kth_power_of_n(n, (k//2) + 1)
    return memo[(n, k)] 

print(kth_power_of_n(2, 5))