from Advent2022.helpers.parse_input import *

input_arr = parse_input(18)

cubes = set()
escaped = set()
trapped = set()
test_set = set()

max_dim = 0

adjacents = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (-1, 0, 0), (1, 0, 0)]

for line in input_arr:
    new_cube = tuple(map(int, line.split(",")))
    max_dim = max(max_dim, *[new_cube[i] + 1 for i in range(3)])
    cubes.add(new_cube)

total = 0

def color(starting_cube):

    global escaped
    to_color = [starting_cube]
    to_color_next = []

    while(to_color):

        for c in to_color:
            #print(len(escaped))
            if c[0] < -1 or c[1] < -1 or c[2] < -1 or c[0] > max_dim or c[1] > max_dim or c[2] > max_dim:
                continue
            if c in cubes or c in escaped:
                continue
    
            escaped.add(c)
            x, y, z = c
            for dx, dy, dz in adjacents:
                to_color_next.append((x + dx, y + dy, z + dz))
        
        to_color = to_color_next
        to_color_next = []


color((0, 0, 0))

for x, y, z in cubes:

    for dx, dy, dz in adjacents:
        test_cube = (x + dx, y + dy, z + dz)

        if test_cube in escaped:
            total += 1

print(total)

