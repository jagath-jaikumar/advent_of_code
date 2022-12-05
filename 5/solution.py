# Advent of Code, Day 5
import os
import re

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

def startup():
  with open(input_path) as f:
    everything = f.read().split("\n")

  instruction_split_line = everything.index("")
  containers_line = instruction_split_line - 1
  n_containers = int(list(filter(None, everything[containers_line].split(" ")))[-1])

  containers = [[] for _ in range(n_containers)]

  for i in range(containers_line-1, -1, -1):
    container_line = re.findall('....',everything[i] + " ")
    for index, container in enumerate(container_line):
      container = container.strip()
      if container:
        containers[index].append(container)

  instructions = everything[instruction_split_line+1:]

  return instructions, containers

def part_1():
  instructions, containers = startup()

  for instruction in instructions:
    _ = instruction.split(" ")
    quantity_, from_, to_ = int(_[1]), int(_[3])-1, int(_[5])-1
    for i in range(quantity_):
      containers[to_].append(containers[from_].pop())

  return "".join([stack[-1][1] for stack in containers])

def part_2():
  instructions, containers = startup()

  for instruction in instructions:
    _ = instruction.split(" ")
    quantity_, from_, to_ = int(_[1]), int(_[3])-1, int(_[5])-1

    to_move = []
    for i in range(quantity_):
      to_move.append(containers[from_].pop())
    to_move.reverse()
    containers[to_].extend(to_move)

  return "".join([stack[-1][1] for stack in containers])
    