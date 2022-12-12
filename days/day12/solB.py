from Advent2022.helpers.parse_input import *
import math

input_arr = parse_input(12)

queue_to_parse = []
have_parsed = set([])
finish = (math.inf, math.inf)

total_rows = len(input_arr)
total_cols = len(input_arr[0])

movements = [(-1, 0), (1, 0), (0, 1), (0, -1)]

input_arr = [list(line.replace('S', 'a')) for line in input_arr]

#Find start
for row, line in enumerate(input_arr):
    for col, char in enumerate(line):

        if char == 'E':
            queue_to_parse.append(((row, col), 0))
            have_parsed.add((row, col))
            input_arr[row][col] = 'z'

while(len(queue_to_parse) > 0):

    (row, col) = queue_to_parse[0][0]
    steps = queue_to_parse[0][1]
    queue_to_parse = queue_to_parse[1:]

    if(input_arr[row][col] == 'a'):
        print(steps)

    for m in movements:
        next_row = row + m[0]
        next_col = col + m[1]

        if next_row >= 0 and next_col >= 0 and next_row < total_rows and next_col < total_cols and (next_row, next_col) not in have_parsed: 

            num = ord(input_arr[row][col])
            next_num = ord(input_arr[next_row][next_col])

            if next_num - num >= -1:
                queue_to_parse.append(((next_row, next_col), steps + 1))
                have_parsed.add((next_row, next_col))




    

    


