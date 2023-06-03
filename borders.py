def inputNum(number):
    if number < 1 or number > 10:
        return 0
    return 1

def inputNum2(number, a):
    if a < number:
        return 0
    else:
        a -= number
    return 1

def pcNum(quantity, a):
    while quantity > a:
        return 0
    a -= quantity
    return 1
