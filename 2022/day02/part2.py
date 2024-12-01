#! /bin/python3




def compute_score(he, round):
    shape = {"A": 1, "B": 2, "C": 3}
    points = {"X": 0, "Y": 3, "Z": 6}
    my_score = points[round]


    if round == "Y":
        # draw
        my_score += shape[he]
    elif round == "Z":
        # I win
        if he == "A":
            my_score += shape["B"]
        elif he =="B":
            my_score += shape["C"]
        else:
            my_score += shape["A"]
    else:
        # I loose
        if he == "A":
            my_score += shape["C"]
        elif he =="B":
            my_score += shape["A"]
        else:
            my_score += shape["B"]


    return my_score



score = 0
with open("input", "r") as f:
    for l in f:
        choices = l.strip().split()
        score += compute_score(he = choices[0], round = choices[1])



print(score)
