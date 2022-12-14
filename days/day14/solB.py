from Advent2022.helpers.parse_input import *

input_arr = parse_input(14)
rock_lines = [line.split(" -> ") for line in input_arr]
ceiling = [['.' for _ in range(200)] for __ in range(1000)]

max_y = 0

for line in rock_lines:

    last_coord = None

    for coord in line:
        (x, y) = tuple(map(int, coord.strip().split(",")))

        ceiling[x][y] = '#'

        if last_coord:
            (lx, ly) = last_coord
            for i in range(min(x, lx), max(x, lx) + 1):
                for j in range(min(y, ly), max(y, ly) + 1):
                    ceiling[i][j] = '#'
                    max_y = max(j, max_y)
        
        last_coord = (x, y)

for line in ceiling:
    line[max_y + 2] = '#'

sand_counter = 0

for sand_counter in range(1, 200 * 1000):

    sx, sy = 500, 0
    fallen = True

    while fallen and sy < 199:

        fallen = False

        for dx in [0, -1, 1]:
            if ceiling[sx + dx][sy + 1] == '.':
                sx, sy = sx + dx, sy + 1
                fallen = True
                break
                
        if not fallen:
            ceiling[sx][sy] = 'o'

    if ceiling[500][0] == 'o':
        print(sand_counter)
        exit(0)


