'''
Problem Statement and Explanation: Narasimha Karumanchi's Algorithm Design Patterns
'''

def climb_stairs(n):
    table = [None]*n
    # note that step no. = i+1  
    table[0] = 1 # no. of ways you can climb 1 stair ((1, 0))
    table[1] = 2 # no. of ways you can climb 2 stairs ((1, 1), (2, 0))
    table[2] = 3 # no. of ways you can climb 3 stairs ((1, 2), (2, 1), (3, 0))
    for i in range(3, n):
        table[i] = table[i-1] + table[i-2] + table[i-3]
    return table[n-1]

print(climb_stairs(5))