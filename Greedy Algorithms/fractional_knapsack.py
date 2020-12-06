'''
Problem: https://www.sanfoundry.com/python-program-solve-fractional-knapsack-problem-using-greedy-algorithm/
'''

def fractional_knapsack(value, weight, capacity):
    '''
    value[i] - value of ith item
    weigth[i] - weight of ith item
    capacty - max capacity our knapsack can hold

    our goal is to fill the knapsack with max value
    '''
    n = len(value)
    ratio = [v/w for v, w in zip(value, weight)]
    indices = list(range(len(n)))
    fractions = [0]*n
    
    indices.sort(key=lambda x: ratio[x], reverse=True)

    total_value = 0
    for i in indices:
        if weight[i] <= capacity:
            fractions[i] = 1
            capacity -= weight[i]
            total_value += value[i]
        else:
            fractions[i] = capacity/weight[i]
            total_value += value[i] * capacity/weight[i]
            break
    return fractions, total_value

