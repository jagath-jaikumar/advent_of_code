# Advent of Code, Day 6
import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

def helper(unique_sequence_length):
  with open(input_path) as f:
    everything = f.read()
  
  for i in range(len(everything) - unique_sequence_length):
    if len(set(everything[i:i+unique_sequence_length])) == unique_sequence_length:
      return i + unique_sequence_length

def part_1():
  return helper(4)


def part_2():
  return helper(14)
    