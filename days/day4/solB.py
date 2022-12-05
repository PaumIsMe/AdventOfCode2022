from Advent2022.helpers.parse_input import *

input_arr = split_array(parse_input(4), ",")

overlaps = 0

for [first, second] in input_arr:
    [low_one, high_one] = [int(i) for i in first.split('-')]
    [low_two, high_two] = [int(i) for i in second.split('-')]
    if not (high_one < low_two or high_two < low_one):
        overlaps += 1
        print(overlaps)
