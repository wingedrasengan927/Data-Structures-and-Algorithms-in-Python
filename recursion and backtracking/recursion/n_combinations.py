'''
choose m elements from n elements
nCm = n!/(n-m)! * m!

The problem with using the formula is n! becomes too big and it might not fit the integer representation

The other way is to use recursion. The recurrence relation would be:
nCm = n-1Cm-1 + n-1Cm
'''
memo = dict()
def n_choose_m(n, m):
    if n == m or m == 0:
        return 1
    if (n, m) in memo:
        return memo[(n, m)]
    memo[(n, m)] = n_choose_m(n-1, m-1) + n_choose_m(n-1, m)
    return memo[(n, m)]

print(n_choose_m(52, 5))