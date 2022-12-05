import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")


def part_1():
    with open(input_path) as f:
        elves = f.read().split("\n\n")

    max_elf_sum = -1
    for elf in elves:
        elf_sum = sum([int(_) for _ in elf.split("\n")])
        if elf_sum > max_elf_sum:
            max_elf_sum = elf_sum

    return max_elf_sum


def part_2():
    with open(input_path) as f:
        elves = f.read().split("\n\n")

    elf_sums = [sum([int(_) for _ in elf.split("\n")]) for elf in elves]

    return sum(sorted(elf_sums, reverse=True)[:3])
