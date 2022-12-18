from Advent2022.helpers.parse_input import *

input_arr = parse_input(18)
cubes = set()
total = 0

for line in input_arr:
    cubes.add(tuple(map(int, line.split(","))))

adjacents = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (-1, 0, 0), (1, 0, 0)]

for x, y, z in cubes:

    for dx, dy, dz in adjacents:

        if (x + dx, y + dy, z + dz) not in cubes:
            total += 1

print(total)

