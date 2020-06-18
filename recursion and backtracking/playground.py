'''
Permutations
'''

def string_permutations(i, stringList):
    if i == len(stringList):
        print("".join(stringList))
    for k in range(i, len(stringList)):
        stringList[i], stringList[k] = stringList[k], stringList[i]
        string_permutations(i+1, stringList)
        stringList[i], stringList[k] = stringList[k], stringList[i]

string_permutations(0, ["b", "o", "a", "t"])