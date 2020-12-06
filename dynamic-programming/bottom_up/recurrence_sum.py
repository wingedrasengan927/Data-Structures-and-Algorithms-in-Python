'''
F(0) = F(1) = 2
F(n) = sum(2*F(i)*F(i-1) for i in range(1, n))
'''

def f(n):
    table = [0]*(n+1)
    table[0] = 2
    table[1] = 2
    table[2] = 2*table[1]*table[0]
    for i in range(3, n+1):
        table[i] = table[i-1] + 2*table[i-1]*table[i-2]
    return table[n]