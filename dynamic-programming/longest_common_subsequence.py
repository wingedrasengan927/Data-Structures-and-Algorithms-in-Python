'''
Problem Statement and Explanation: Narasimha Karumanchi's Algorithm Design Patterns
'''

def LCS_length(X, Y):
    memo = dict()
    LCS_length = dp(0, 0, X, Y, memo)
    return LCS_length

def dp(i, j, X, Y, memo):
    if i == len(X) or j == len(Y):
        return 0

    if (i, j) in memo:
        return memo[(i, j)]

    if X[i] == Y[j]:
        memo[(i, j)] = 1 + dp(i+1, j+1, X, Y, memo)

    else:
        memo[(i, j)] = max(dp(i+1, j, X, Y, memo), dp(i, j+1, X, Y, memo))

    return memo[(i, j)]

string1 = "ABCBDAB"
string2 = "BDCABA"

print(LCS_length(string1, string2))