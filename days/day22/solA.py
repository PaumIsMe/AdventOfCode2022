from Advent2022.helpers.parse_input import *

arr = [list(line[:-1]) for line in open(get_input_path(22))]
instr = ''.join(arr[-1])
arr = arr[:-2]

px = 0
py = 0

MAX_X = 0
MAX_Y = len(arr)

for line in arr:
    MAX_X = max(MAX_Y, len(line))

for line in arr:
    while len(line) < MAX_X:
        line.append(' ')

dpx = [1, 0, -1, 0]
dpy = [0, 1, 0, -1]

i_pointer = 0
direction = 0

while arr[0][px] == ' ':
    px += 1

def read_instruction(x):
    global px
    global py
    global i_pointer
    global direction

    if instr[x] == 'L':
        i_pointer += 1
        direction = (direction - 1) % 4
        return 0
    
    if instr[x] == 'R':
        i_pointer += 1
        direction = (direction + 1) % 4
        return 0
    
    i_pointer = x
    while i_pointer < len(instr) and ord(instr[i_pointer]) >= ord('0') and ord(instr[i_pointer]) <= ord('9'):
        i_pointer += 1

    print(instr[x:i_pointer])
    return int(instr[x:i_pointer])

def step():

    global px
    global py
    global direction

    MAX_X = len(arr[py])

    nx = px
    ny = py
    nd = direction
    
    nx = (nx + dpx[direction]) % MAX_X
    ny = (ny + dpy[direction]) % MAX_Y

    #print("Pre: ", nx, ny)
    if arr[ny][nx] == ' ':
        nx = (nx + dpx[direction]) % MAX_X
        ny = (ny + dpy[direction]) % MAX_Y
        #print("Post: ", nx, ny)

    if arr[ny][nx] == '#':
        return
    elif arr[ny][nx] == '.':
        py = ny
        px = nx
        return
    else:
        assert(False)


print(len(arr))
print(arr[-1])

while(i_pointer < len(instr)):
    num_steps = read_instruction(i_pointer)
    for _ in range(num_steps):
        step()

print(px, py, direction)
print(1000 * (py + 1) + 4 * (px + 1) + direction)


