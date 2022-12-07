# Advent of Code, Day 7
import os
from collections import deque

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

class Directory:
  def __init__(self, name, parent):
    self.name = name
    self.parent = parent

    self.total_size = -1
    self.subdirectories = {}
    self.files = []

class File:
  def __init__(self, name, size):
    self.name = name
    self.size = size

def create_tree():
  with open(input_path) as f:
    terminal = f.read().split("\n")

  instruction_clusters = []
  line_index = 0
  while line_index < len(terminal)-1:
    current_instruction_set = [terminal[line_index]]
    while line_index < len(terminal)-1 and not terminal[line_index+1].startswith("$"):
      current_instruction_set.append(terminal[line_index+1])
      line_index += 1
    line_index += 1
    instruction_clusters.append(deque(current_instruction_set))
  
  root = Directory("root", None)
  root.subdirectories["/"] =  Directory("/", root)

  cwd = root

  for instruction_cluster in instruction_clusters:
    instruction = instruction_cluster.popleft().split(" ")
    if instruction[1] == 'cd':
      subdir = instruction[2]
      if subdir == '..':
        cwd = cwd.parent
      else:
        cwd = cwd.subdirectories[subdir]

    if instruction[1] == 'ls':
      outputs = [_.split() for _ in list(instruction_cluster)]
      for output in outputs:
        if output[0] == 'dir':
          cwd.subdirectories[output[1]] = Directory(output[1], cwd)
        
        else:
          cwd.files.append(File(output[1], int(output[0])))
  
  def calculate_sums(node):
    if len(node.subdirectories) == 0:
      node.total_size = sum(f.size for f in node.files)
      return
    
    for _,n in node.subdirectories.items():
      calculate_sums(n)

    node.total_size = sum(f.size for f in node.files) + sum(d.total_size for _, d in node.subdirectories.items())

  calculate_sums(root)
  
  return root

def part_1():
  root = create_tree()
  q = deque([root])
  summ = 0

  while q:
    p = q.popleft()
    if p.total_size <= 100000:
      summ += p.total_size
    
    for _, sub in p.subdirectories.items():
      q.append(sub)
  
  return summ

def part_2():
  root = create_tree()

  total_space = 70000000
  necessary_unused_space = 30000000
  used_space = root.total_size
  desired_space_reduction = necessary_unused_space - (total_space - used_space)

  q = deque([root])
  summ = 0

  solution = float('inf')
  while q:
    p = q.popleft()
    if p.total_size > desired_space_reduction and p.total_size < solution:
      solution = p.total_size
    
    for _, sub in p.subdirectories.items():
      q.append(sub) 
  
  return solution