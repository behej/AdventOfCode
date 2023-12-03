#!/usr/bin/python3


def char2number(c):
    return ord(c) - ord('0')

spelled_digits = {'one':1, 
                  'two': 2,
                  'three': 3, 
                  'four': 4, 
                  'five':5, 
                  'six': 6, 
                  'seven': 7, 
                  'eight': 8, 
                  'nine': 9}


sum = 0
with open("input.txt", "r") as f:
    for l in f:
        # Main idea is to replace string represented digits by their equivalent in real digits
        # and then process the line as per part 1.
        # The problem is that strings can overlap (ex: oneight). If 'one' is replaced by '1', 
        # string turns '1ight' and the 'eight' is missed. The trick is to replace the string by
        # '<string><digit><string>'. The string is kept before and after for combination with
        # other letters and the digit is inserted for later findings (eg 'oneight' will turn
        # successiverly 'one1oneight' and then 'one1oneight8eight)
        for (k, v) in spelled_digits.items():
            l = l.replace(k, "{}{}{}".format(k, v, k))

        digits = [c for c in l if c.isdigit()]
        value = char2number(digits[0]) * 10 + char2number(digits[-1])
        sum += value
       
print(sum)