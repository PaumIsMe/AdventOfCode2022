from Advent2022.helpers.parse_input import *
import numpy as np

visited = set()
visited.add((0, 0))

rope = [[0, 0] for i in range(10)]

vectors = {'U': (0, 1), 'R': (1, 0), 'L': (-1, 0), 'D': (0, -1)}

for line in parse_input(9):
    direction, num_movements = line.split(' ')

    for i in range(int(num_movements)):
        head_movement = vectors[direction]
        rope[0][0] += head_movement[0]
        rope[0][1] += head_movement[1]

        for k in range(1, 10):

            knot = rope[k]
            prev = rope[k - 1]

            if abs(knot[0] - prev[0]) >= 2 or abs(knot[1] - prev[1]) >= 2:
                knot[0] += np.sign(prev[0] - knot[0])
                knot[1] += np.sign(prev[1] - knot[1])

            else:
                break
        
        visited.add(tuple(rope[9]))

print(len(list(visited)))