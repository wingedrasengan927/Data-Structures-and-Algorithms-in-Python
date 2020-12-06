def fibonacci_dp(n):
    table = [None]*(n+1)
    for i in range(n+1):
        if i == 0 or i == 1:
             table[i] = i
        else:
            table[i] = table[i-1] + table[i-2]
    return table[n]

print(fibonacci_dp(4))    