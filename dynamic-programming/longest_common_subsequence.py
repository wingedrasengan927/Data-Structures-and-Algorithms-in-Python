'''
Problem Statement and Explanation: Narasimha Karumanchi's Algorithm Design Patterns
'''

def LCS_length(X, Y):
    m = len(X)
    n = len(Y)
    memo = dict()
    LCS_length = dp(m-1, n-1, X, Y, memo)
    return LCS_length

def dp(i, j, X, Y, memo):
    if i < 0 or j < 0:
        return 0

    if (i, j) in memo:
        return memo[(i, j)]

    if X[i] == Y[j]:
        memo[(i, j)] = 1 + dp(i-1, j-1, X, Y, memo)

    else:
        memo[(i, j)] = max(dp(i-1, j, X, Y, memo), dp(i, j-1, X, Y, memo))

    return memo[(i, j)]

string1 = "AGGTAB"
string2 = "GXTXAYB"

print(LCS_length(string1, string2))