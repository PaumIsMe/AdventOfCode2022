from Advent2022.helpers.parse_input import *

input_arr = parse_input(3)
sum = 0

for i in range(0, len(input_arr), 3):
    s1 = input_arr[i]
    s2 = input_arr[i + 1]
    s3 = input_arr[i + 2]

    val = list(set(s1) & set(s2) & set(s3))[0]
    val = ord(val)

    if val >= ord("a"):
        sum += val - ord("a") + 1
    else:
        sum += val - ord("A") + 26 + 1

print(sum)