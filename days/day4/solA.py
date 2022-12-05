from Advent2022.helpers.parse_input import *

input_arr = split_array(parse_input(4), ",")

overlaps = 0

for [first, second] in input_arr:
    [low_one, high_one] = [int(i) for i in first.split('-')]
    [low_two, high_two] = [int(i) for i in second.split('-')]
    if ( (low_one <= low_two) and (high_one >= high_two)) or ((low_two <= low_one) and (high_two >= high_one)):
        overlaps += 1
        print(overlaps)
