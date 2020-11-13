'''
Find the kth odd natural number. 1 being the first natural number
ans: 2*(k-1) + 1
'''

def kth_odd_num(k):
    if k == 1:
        return 1
    return kth_odd_num(k-1) + 2

print(kth_odd_num(8))