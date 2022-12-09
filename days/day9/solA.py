from Advent2022.helpers.parse_input import *
import numpy as np

score = 0

visited = set([(0, 0)])

head_position = [0, 0]
tail_position = [0, 0]

vectors = {'U': (0, 1), 'R': (1, 0), 'L': (-1, 0), 'D': (0, -1)}

for line in parse_input(9):
    direction, num_movements = line.split(' ')

    for i in range(int(num_movements)):
        head_movement = vectors[direction]
        head_position[0] += head_movement[0]
        head_position[1] += head_movement[1]

        if abs(head_position[0] - tail_position[0]) >= 2 or abs(head_position[1] - tail_position[1]) >= 2:
            tail_position[0] += np.sign(head_position[0] - tail_position[0])
            tail_position[1] += np.sign(head_position[1] - tail_position[1])
        
        visited.add(tuple(tail_position))

print(len(list(visited)))