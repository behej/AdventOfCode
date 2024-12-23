#! /usr/bin/python3

from collections import namedtuple

Button = namedtuple('Button', ['x', 'y'])
Prize = namedtuple('Prize', ['x', 'y'])
Combo = namedtuple('Combo', ['btnA', 'btnB'])


def compute_price(c):
    return (3 * c.btnA) + (1 * c.btnB)


def find_combinations(btnA, btnB, prize):
    maxPushesOnA = prize.x // btnA.x

    combinations = []
    for i in range(maxPushesOnA, -1, -1):
        if (prize.x - (i * btnA.x)) % btnB.x == 0:
            c = Combo(i, (prize.x - (i * btnA.x)) // btnB.x)

            if (btnA.y * c.btnA) + (btnB.y * c.btnB) == prize.y:
                combinations.append(c)
    return combinations


def find_cheapest_combination(combinations):
    cheapest = None
    for c in combinations:
        if cheapest is None or compute_price(c) < compute_price(cheapest):
            cheapest = c
    return cheapest



sum = 0

with open("input", "r") as f:
    lines = f.readlines()
    lines = [l for l in lines if l != "\n"]

    for (btnA, btnB, prize) in zip(lines[::3], lines[1::3], lines[2::3]):
        btnA = Button(int(btnA.split(" ")[2].split("+")[1][:-1]), int(btnA.split(" ")[3].split("+")[1]))
        btnB = Button(int(btnB.split(" ")[2].split("+")[1][:-1]), int(btnB.split(" ")[3].split("+")[1]))
        prize = Prize(int(prize.split(" ")[1].split("=")[1][:-1]), int(prize.split(" ")[2].split("=")[1]))

        combinations = find_combinations(btnA, btnB, prize)
        c = find_cheapest_combination(combinations)

        if c:
            sum += compute_price(c)


print(sum)




