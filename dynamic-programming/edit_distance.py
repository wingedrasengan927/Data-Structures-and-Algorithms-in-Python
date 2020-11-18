'''
Problem: https://www.python-course.eu/levenshtein_distance.php
'''

def edit_distance(X, Y):
    memo = dict()
    result = dp(0, 0, X, Y, memo)
    return result

def dp(i, j, X, Y, memo):
    # base case
    if i == len(X): # we have reached the end of X, our only option now is to insert all chars from Y into X
        return len(Y) - j
    elif j == len(Y): # we have reached the end of Y, our only option now is to remove remaining chars from X
        return len(X) - i

    # memoization
    if (i, j) in memo:
        return memo[(i, j)]

    # if both chars are same
    if X[i] == Y[j]:
        return dp(i+1, j+1, X, Y, memo)

    cost = 1 # we are assuming that the cost of insert and delete and replace is the same and is 1

    # replace, insert, delete
    memo[(i, j)] = min(cost + dp(i+1, j+1, X, Y, memo), cost + dp(i, j+1, X, Y, memo), cost + dp(i+1, j, X, Y, memo))
    return memo[(i, j)]
    
print(edit_distance("sunday", "saturday"))
print(edit_distance("Python", "Peithel"))