from Advent2022.helpers.parse_input import *

input_arr = parse_input(15)

no_beacon = set()
are_beacons = set()
becons_on_line = 0

LINE_NUM = 2000000

for line in input_arr:
    split_line = line.split(' ')
    sx = int(split_line[2][2:-1])
    sy = int(split_line[3][2:-1])
    bx = int(split_line[8][2:-1])
    by = int(split_line[9][2:])

    if by == LINE_NUM:
        are_beacons.add(bx)

    distance = abs(sx - bx) + abs(sy - by)

    distance_to_row = abs(sy - LINE_NUM)

    remainder = distance - distance_to_row

    if remainder >= 0:
        for i in range(remainder * -1, remainder + 1):
            no_beacon.add(sx + i)
    
print(len(no_beacon - are_beacons))


