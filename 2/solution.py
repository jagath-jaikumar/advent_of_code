import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")


def part_1():
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    lookup = {
        "A": ROCK,
        "X": ROCK,
        "B": PAPER,
        "Y": PAPER,
        "C": SCISSORS,
        "Z": SCISSORS,
    }
    with open(input_path) as f:
        plays = f.read().split("\n")

    summ = 0
    for play in plays:
        opponent, me = lookup[play[0]], lookup[play[-1]]

        if (
            opponent == SCISSORS
            and me == PAPER
            or opponent == PAPER
            and me == ROCK
            or opponent == ROCK
            and me == SCISSORS
        ):
            summ += me
        elif opponent == me:
            summ += me + 3
        else:
            summ += me + 6

    print(summ)


def part_2():
    with open(input_path) as f:
        plays = [_.replace(" ", "") for _ in f.read().split("\n")]

    scores = {
        "AX": 3,
        "BX": 1,
        "CX": 2,
        "AY": 3 + 1,
        "BY": 3 + 2,
        "CY": 3 + 3,
        "AZ": 6 + 2,
        "BZ": 6 + 3,
        "CZ": 6 + 1,
    }

    summ = sum([scores[play] for play in plays])

    print(summ)
