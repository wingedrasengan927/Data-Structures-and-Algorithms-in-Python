'''
Reference: https://brilliant.org/wiki/recursive-backtracking/
Given a string of length N, find all its permutations
'''

def permuation(stringList, i):
    if i == len(stringList):
        print("".join(stringList))
    for k in range(i, len(stringList)):
        stringList[k], stringList[i] = stringList[i], stringList[k] # swap i, k
        permuation(stringList, i+1)
        stringList[k], stringList[i] = stringList[i], stringList[k] # backtracking

permuation(['b', 'o', 'a', 't'], 0)