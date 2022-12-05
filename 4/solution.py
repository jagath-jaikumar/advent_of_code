import os
from typing import List

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

def part_1():
    with open(input_path) as f:
        assignments = f.read().split("\n")
    
    summ = 0
    for assignment in assignments:
        assignment1, assignment2 = assignment.split(",")

        a11, a12 = assignment1.split("-")
        a21, a22 = assignment2.split("-")

        a11, a12 = int(a11), int(a12)
        a21, a22 = int(a21), int(a22)

        if (a11 <= a21 and a12 >= a22) or (a21 <= a11 and a22 >= a12):
            summ+=1
    
    return summ

def part_2():
    with open(input_path) as f:
        assignments = f.read().split("\n")
    
    summ = 0
    for assignment in assignments:
        assignment1, assignment2 = assignment.split(",")

        a11, a12 = assignment1.split("-")
        a21, a22 = assignment2.split("-")

        def is_overlapping(x1,x2,y1,y2):
            return max(x1,y1) <= min(x2,y2)

        if is_overlapping(int(a11), int(a12), int(a21), int(a22)):
            summ+=1
    
    return summ