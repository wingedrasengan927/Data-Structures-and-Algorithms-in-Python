'''
Problem Statement: https://www.geeksforgeeks.org/python-program-for-activity-selection-problem-greedy-algo-1/
'''

def maximizeActivitySelection(s, f):
    # s[i] - start time of ith task
    # f[i] - finish time of ith task

    n = len(s)

    # first we sort the array based on finishing times
    s = [x for x, _ in sorted(zip(s, f), key=lambda i: i[1])]
    f = sorted(f)

    # we always select the first activity
    i = 0
    count = 1

    for j in range(1, n):
        # if the start time of the current activity if
        # greater than the finish time of the last activity
        # we select it
        if s[j] >= f[i]:
            count += 1
            i = j
    
    return count