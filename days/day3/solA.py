from Advent2022.helpers.parse_input import *

def character_value(c):
    return ord(c) - 38 if c.isupper() else ord(c) - 96

input_arr = parse_input(3)

priority_sum = 0

for line in input_arr:

    line_len = len(line) // 2

    if line_len == 0:
        break

    compartment_one = set(line[:line_len])
    compartment_two = set(line[line_len:])

    letter = list(compartment_one.intersection(compartment_two))[0]
    priority_sum += character_value(letter)

print(priority_sum)

