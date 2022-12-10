from Advent2022.helpers.parse_input import *

input_arr = parse_input(10)

c = 1
v = 1
arr = [[0 for i in range(0, 40)] for i in range(0, 6)]

def draw(a, v, t):
    x = (t - 1) % 40
    y = (t - 1) // 40

    if y < 6:
        a[y][x] = '#' if abs(v - x) <= 1 else '.'

for line in input_arr:
    draw(arr, v, c)
    c += 1

    if line[0] == 'a':
        draw(arr, v, c)
        c += 1
        v += int(line.split(" ")[1])

print_array(arr)

