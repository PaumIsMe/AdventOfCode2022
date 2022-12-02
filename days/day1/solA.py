from Advent2022.helpers.parse_input import *

input_arr = convert_to_int(parse_input(1))
print(input_arr)

current_calories = 0
top_calories = 0

for num in input_arr:
    if num == None:
        top_calories = max(top_calories, current_calories)
        current_calories = 0
    else:
        current_calories += num

print(top_calories)
