#! /usr/bin/python3


sum = 0


def concat(val1, val2):
    return int(str(val1) + str(val2))


def test_values(res, val, l):
    if len(l) == 1:
        if val + l[0] == res:
            return True
        if val * l[0] == res:
            return True
        if concat(val, l[0]) == res:
            return True
        
    else:
        if test_values(res, val + l[0], l[1:]):
            return True
        elif test_values(res, val * l[0], l[1:]):
            return True
        elif test_values(res, concat(val, l[0]), l[1:]):
            return True
        else:
            return False





with open("input", "r") as f:
    for l in f:
    
        result = int(l.split(":")[0])
        values = l.split(":")[1]

        values = [int(i) for i in values.split()]
        
        if test_values(result, values[0], values[1:]):
            sum += result



print(sum)
