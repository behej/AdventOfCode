#! /bin/python3


def convert_choice(letter):
    if letter in ["A", "X"]:
        return "Rock"
    elif letter in ["B", "Y"]:
        return "Paper"
    elif letter in ["C", "Z"]:
        return "Scissors"


def compute_score(he, me):
    shape = {"Rock": 1, "Paper": 2, "Scissors": 3}
    my_score = shape[me]

    if he == me:
        # draw
        my_score += 3
    elif (he == "Rock" and me == "Paper") or (he == "Paper" and me == "Scissors") or (he == "Scissors" and me == "Rock"):
        # I win
        my_score += 6

    return my_score



score = 0
with open("input", "r") as f:
    for l in f:
        choices = l.strip().split()
        score += compute_score(he = convert_choice(choices[0]), me = convert_choice(choices[1]))



print(score)
