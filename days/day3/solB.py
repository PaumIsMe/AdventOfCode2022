from Advent2022.helpers.parse_input import *

def character_value(c):
    return ord(c) - 38 if c.isupper() else ord(c) - 96

input_arr = parse_input(3)

priority_sum = 0

for idx in range(0, len(input_arr) - 2, 3):

    priority_sum += character_value(list(set(input_arr[idx]).intersection(input_arr[idx + 1]).intersection(input_arr[idx + 2]))[0])

print(priority_sum)
