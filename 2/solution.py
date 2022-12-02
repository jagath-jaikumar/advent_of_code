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
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    lookup = {
        "A": ROCK,
        "B": PAPER,
        "C": SCISSORS,
    }

    with open(input_path) as f:
        plays = f.read().split("\n")

    summ = 0
    for play in plays:
        opponent, expectation = lookup[play[0]], play[-1]

        if expectation == "X":
            if opponent == SCISSORS:
                me = PAPER
            elif opponent == PAPER:
                me == ROCK
            else:
                me = SCISSORS

            summ += me

        elif expectation == "Y":
            me = opponent
            summ += me + 3
        else:
            if opponent == SCISSORS:
                me = ROCK
            elif opponent == PAPER:
                me == SCISSORS
            else:
                me = PAPER

            summ += me + 6

    print(summ)


part_2()
