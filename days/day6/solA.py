from Advent2022.helpers.parse_input import *

SIGNAL_LENGTH = 4

input_str = parse_input(6)[0]

for i in range(len(input_str) - SIGNAL_LENGTH + 1):
    if all_unique(input_str[i:i+SIGNAL_LENGTH]):
        print(i + SIGNAL_LENGTH)
        break
