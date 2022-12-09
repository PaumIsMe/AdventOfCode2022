from Advent2022.helpers.parse_input import *

input_arr = parse_input(4)

total = 0

for line in input_arr:
    a, b, x, z = map(int, line.replace(",", "-").split("-"))
    if (a <= z and b >= x):
        total += 1

print(total)
