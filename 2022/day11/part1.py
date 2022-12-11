#! /usr/bin/python3

class Operation:
    def __init__(self, formula):
        eqn = formula.split('=')[1]
        [self.__op1, self.__op, self.__op2] = eqn.split()
        if self.__op1.isdigit():
            self.__op1 = int(self.__op1)
        if self.__op2.isdigit():
            self.__op2 = int(self.__op2)


    def eval(self, val):
        if isinstance(self.__op1, int):
            a = self.__op1
        elif self.__op1 == 'old':
            a = val
        else:
            print('Error 1')

        if isinstance(self.__op2, int):
            b = self.__op2
        elif self.__op2 == 'old':
            b = val
        else:
            print('Error 2')

        if self.__op == '+':
            return a+b
        elif self.__op == '-':
            return a-b
        elif self.__op == '*':
            return a*b


class Monkey:
    def __init__(self, items, oper, divisor, if_true, if_false):
        self.__items = items
        self.__oper = oper
        self.__divisor = divisor
        self.__if_true = if_true
        self.__if_false = if_false
        self.__counter = 0

    def inspect(self):
        self.__counter += len(self.__items)
        for i in range(len(self.__items)):
            old = self.__items.pop(0)
            new = self.__oper.eval(old)
            new = new // 3
            if (new % self.__divisor == 0):
                monkeys[self.__if_true].get_item(new)
            else:
                monkeys[self.__if_false].get_item(new)

    def get_item(self, item):
        self.__items.append(item)

    def get_count(self):
        return self.__counter


monkeys = []

with open('input', 'r') as f:
    for l in f:
        if l.strip().startswith('Starting items:'):
            items = l.split(':')[-1].split(',')
            items = [int(i) for i in items]
        elif l.strip().startswith('Operation'):
            oper = Operation(l.split(':')[-1])
        elif l.strip().startswith('Test'):
            divisor = int(l.split()[-1])
        elif l.strip().startswith('If true'):
            if_true = int(l.split()[-1])
        elif l.strip().startswith('If false'):
            if_false = int(l.split()[-1])
        elif l.strip() == '':
            monkeys.append(Monkey(items, oper, divisor, if_true, if_false))


for _ in range(20):
    for i, m in enumerate(monkeys):
        m.inspect()


inspections = [m.get_count() for m in monkeys]
inspections.sort(reverse=True)
print(inspections[0] * inspections[1])
