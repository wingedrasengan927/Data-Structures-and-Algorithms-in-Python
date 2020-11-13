def countVowelStrings(n):
    result = []
    vowelsList = ["a", "e", "i", "o", "u"]
    countVowelStringsHelper(n, "", 0, result, vowelsList)
    return result
    
def countVowelStringsHelper(n, current, index, result, vowelsList):
    if len(current) == n:
        result.append(current)
        return
    for idx in range(index, len(vowelsList)):
        vowel = vowelsList[idx]
        countVowelStringsHelper(n, current + vowel, idx, result, vowelsList)

print(countVowelStrings(2))