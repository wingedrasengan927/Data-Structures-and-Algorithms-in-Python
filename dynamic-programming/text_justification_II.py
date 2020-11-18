'''
############## TEXT JUSTIFICATION ###########
'''

import math

list_of_words = ["I", "am", "the", "greatest", "gryphon", "and", "I", "am", "Invincible",
                "Think", "twice", "before", "fighting", "with", "me", "else", "I", "will", 
                "squash", "you", "like", "a", "tennis", "ball", "beware", "for", "I", "am", 
                "the", "guy", "that", "has", "defeated", "shadow"]

page_width = 12

def calc_badness(line, page_width):
    '''
    line - subarray of words to fit in a line
    '''
    line_width = sum(len(word) for word in line)
    if line_width > page_width:
        return float('inf')
    return math.pow(page_width - line_width, 3)

def dp(i, words, page_width, memo, parent_pointers): # solution to the subproblem = words[i:]
    n = len(words)

    # base case: badness is 0 once we reach the end of the array
    # i.e once we reach index n
    if i == n:
        return 0

    # memoization
    if i in memo:
        return memo[i]

    # recurrence relation
    # DP(i) = min(DP(j) + badness(i, j) for j in range(i+1, n+1))
    min_badness = float('inf')
    for j in range(i+1, n+1):
        current_badness = dp(j, words, page_width, memo, parent_pointers) + calc_badness(words[i:j], page_width)
        if current_badness < min_badness:
            min_badness = current_badness
            parent_pointers[i] = j

    memo[i] = min_badness
    return memo[i]

def justify_text(words, page_width):
    # we assume that each word is succeeded by atleast one space
    # and hence we modify the input to include one space after each word
    new_words = []
    for idx, word in enumerate(words):
        new_words.append(word)
        if idx < len(words)-1:
            new_words.append(" ")
    memo = dict()
    parent_pointers = dict()
    dp(0, new_words, page_width, memo, parent_pointers)
    
    # following parent pointers
    key = 0
    while key != None:
        next = parent_pointers.get(key)
        # print(new_words[key:next])
        print("".join(new_words[key:next]))
        key = next

justify_text(list_of_words, page_width)