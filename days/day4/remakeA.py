from Advent2022.helpers.parse_input import *

input_arr = parse_input(4)

total = 0

for line in input_arr:
    a, b, x, z = map(int, line.replace(",", "-").split("-"))
    if (a <= x and b >= z) or (x <= a and z >= b):
        total += 1

print(total)
