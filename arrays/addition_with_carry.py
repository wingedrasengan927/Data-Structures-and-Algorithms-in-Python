'''
Add Two Numbers using Normal way of addition
'''

def convert_numbers_to_list(num):
    result = []
    while num > 0:
        result.append(num%10)
        num = num // 10
    return result[::-1]

def add_two_numbers(num1, num2):
    # convert numbers to list
    num1_list = convert_numbers_to_list(num1)
    num2_list = convert_numbers_to_list(num2)
     
    _sum = 0
    result = []

    for _ in range(max(len(num1_list), len(num2_list))):

        if len(num1_list) > 0:
            _sum += num1_list[-1]
        if len(num2_list) > 0:
            _sum += num2_list[-1]

        place = _sum % 10
        _sum = _sum // 10

        result.append(place)

        num1_list = num1_list[:-1]
        num2_list = num2_list[:-1]

    if _sum != 0:
        result.append(_sum)
    
    result = list(map(str, result))
    result = result[::-1]

    return int("".join(result))

print(add_two_numbers(1224, 1))