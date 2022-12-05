import os
from typing import List

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

alphabet_reference = "*abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open(input_path) as f:
    sacks = f.read().split("\n")


def find_common_char_in_strings(inputs: List[str]) -> str:
    # length 1, assumes common char exists
    return list(set.intersection(*map(set, inputs)))[0]


def part_1():

    summ = sum(
        [
            alphabet_reference.index(
                find_common_char_in_strings(
                    # split sack into equal size compartments
                    [sack[: len(sack) // 2], sack[len(sack) // 2 :]]
                )
            )
            for sack in sacks
        ]
    )

    return summ


def part_2():
    # split sacks into groups of 3
    triplets = [sacks[i : i + 3] for i in range(0, len(sacks), 3)]

    summ = sum(
        [
            alphabet_reference.index(find_common_char_in_strings(triplet))
            for triplet in triplets
        ]
    )

    return summ
