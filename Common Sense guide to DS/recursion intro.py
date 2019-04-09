
# let's implement a simple countdown using recursion

def countdown(time):
    print(time)
    if time==0:
        return
    else:
        return countdown(time-1)
countdown(10)