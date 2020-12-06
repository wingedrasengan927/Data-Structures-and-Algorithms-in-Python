'''
Explanation: https://www.youtube.com/watch?v=ASoaQq66foQ
Algorithm: https://www.programiz.com/dsa/longest-common-subsequence
'''

def LCS_finder(X, Y):
    m = len(X)
    n = len(Y)
    LCS = [[None for j in range(n+1)] for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                LCS[i][j] = 0
            elif X[i-1] == Y[j-1]:
                LCS[i][j] = 1 + LCS[i-1][j-1]
            else:
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

    LCS_length = LCS[m][n] # length of the common subsequence

    subsequence = [""]*LCS_length
    i, j = m, n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            subsequence[LCS_length-1] = X[i-1]
            i -= 1
            j -= 1
            LCS_length -= 1

        elif LCS[i-1][j] > LCS[i][j-1]:
            i -= 1
        else:
            j -= 1

    return "".join(subsequence)

X = "AGGTAB"
Y = "GXTXAYB"

print(LCS_finder(X, Y))