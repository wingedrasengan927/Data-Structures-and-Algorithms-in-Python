'''
A turnstile is installed at a university, and the students can exit or enter through it.
it takes 1s to pass through the turnstile. Given an input of time and direction, where 
time[i] indicates the second when the person would be entering and drection[i] indicates 
whether he wants to enter or exit.
if two students enter or exit at the same time i.e t[i] is same for them,
then we apply the following conditions:
1. if prev State of turnstile is reset or exit, then exit guy will be given preference
2. if prevState is enter, then enter guy will be preferred
'''

from collections import deque

def getLeaveTime(incomingTime, direction):
    '''
    1. The idea is we separate the input into two queues, one for exit and one for enter
    2. we maintain a time counter - currentTime which represents the current time
    3. we process the enter and exit queues until they both are empty
    4. we process the exit queue i.e we let the person who wants to exit pass if:
        a. his time is less than or equal to the current time
        b. the previous state of turnstile is 1 or -1
        c. or the previous state of turnstile is 0 but the person in enter queue hasn't come yet
        d. or enter queue is empty and exit queue is not empty
    5. if the above condition satisfies, we let the person leave first and update prevState 
    6. next checking the conditions of the enter queue, we let the person enter and update prevState
    7. since we are already checking the conditions for the exit queue, we don't need to check all of them
    for the enter queue
    8. we update our currentTime after each step

    '''
    prevState = -1 # previous state of the turnstile
    result = [0] * len(incomingTime)
    exit = deque()
    enter = deque()
    i = 0
    for time, dir in zip(incomingTime, direction):
        if dir == 0:
            enter.append([time, i])
        else:
            exit.append([time, i])
        i += 1
    currentTime = 0
    while enter or exit:
        if exit and exit[0][0] <= currentTime and ((prevState == -1 or prevState == 1) or \
        len(enter) == 0 or (enter[0][0] > currentTime and prevState == 0)):
            val = exit.popleft()
            result[val[1]] = currentTime
            prevState = 1
        elif len(enter) > 0 and enter[0][0] <= currentTime:
            val = enter.popleft()
            result[val[1]] = currentTime
            prevState = 0
        else:
            # reset the prev State since nobody is there to pass through
            prevState = -1

        currentTime += 1

    return result

time = [0,0,1,5]
direction = [0,1,1,0]
assert getLeaveTime(time, direction) == [2,0,1,5]
