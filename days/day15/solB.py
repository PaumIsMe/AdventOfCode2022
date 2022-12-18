from Advent2022.helpers.parse_input import *

input_arr = parse_input(15)

pos = set()
impos = set()
sensor_beacons = []
becons_on_line = 0

for line in input_arr:
    split_line = line.split(' ')
    sx = int(split_line[2][2:-1])
    sy = int(split_line[3][2:-1])
    bx = int(split_line[8][2:-1])
    by = int(split_line[9][2:])
    sensor_beacons.append((sx, sy, abs(sx - bx) + abs(sy - by)))


def find_uncovered(depth, start_x, start_y):
    max_size = 4000000 // (10**(depth))

    if max_size <= 4:
        #print("Close...")
        for dx in range(0, max_size):
            for dy in range(0, max_size):
                cx = start_x + dx
                cy = start_y + dy
                found_overlap = False
                for sb in sensor_beacons:
                    sx, sy, distance = sb
                    if abs(cx - sx) + abs(cy - sy) <= distance:
                        found_overlap = True
                        break
                if not found_overlap:
                    return (True, start_x + dx, start_y + dy)
        return (False, 0, 0)
    
    arr_size = 10

    possibles = [[True for _ in range(arr_size)] for __ in range(arr_size)]
    check_distance = max_size // arr_size

    for sb in sensor_beacons:
        sx, sy, distance = sb
        for i, x in enumerate(range(start_x, start_x + max_size, check_distance)):
            for j, y in enumerate(range(start_y, start_y + max_size, check_distance)):
                within_range = [abs(cx - sx) + abs(cy - sy) <= distance for cx, cy in [(x, y), (x + check_distance - 1, y), (x, y + check_distance - 1), (x + check_distance - 1, y + check_distance - 1)]]
                if all(within_range):
                    possibles[i][j] = False
                
    for i, row in enumerate(possibles):
        for j, truth in enumerate(row):
            if truth:
                result = find_uncovered(depth + 1, start_x + i * check_distance, start_y + j * check_distance)
                if result[0]:
                    return result
    
    return (False, 0, 0)

result = find_uncovered(0, 0, 0)
print(result[1] * 4_000_000 + result[2])
