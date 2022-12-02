from Advent2022.helpers.parse_input import *
import bisect

def adjust_top_calories(arr, num):
    arr = arr.sort

input_arr = convert_to_int(parse_input(1))
print(input_arr)

current_calories = 0
top_calories = [0, 0, 0]

for num in input_arr:
    if num == None:
        if current_calories > top_calories[0]:
            bisect.insort(top_calories, current_calories)
            top_calories = top_calories[1:]

        current_calories = 0
    else:
        current_calories += num

print(top_calories)
print(sum(top_calories))
