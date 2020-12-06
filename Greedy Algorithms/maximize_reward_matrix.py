'''
Problem Statement: https://algodaily.com/lessons/getting-to-know-greedy-algorithms-through-examples?view=article
'''

def maximizeReward(matrix):
    # start cell - (0, 0)
    # goal cell - (m, n)
    # can only move right or down
    m = len(matrix)-1
    n = len(matrix[0])-1

    i, j = 0, 0
    curr_cost  = 0

    while (i, j) != (m, n):
        curr_cost += matrix[i][j]
        if i == m:
            j += 1
            continue
        if j == n:
            i += 1
            continue

        if matrix[i+1][j] > matrix[i][j+1]:
            i += 1
        else:
            j += 1
    
    return curr_cost + matrix[m][n]

test = [[5, 20, 36], [4, 34, 32], [100, 23, 45]] # expected 138
print(maximizeReward(test))
