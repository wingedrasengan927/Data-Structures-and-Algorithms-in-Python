def factorial_dp(n):
    table = [None]*(n+1)
    for i in range(n+1):
        if i == 0 or i == 1:
            table[i] = 1
        else:
            table[i] = i*table[i-1]
    return table[n]

print(factorial_dp(4))