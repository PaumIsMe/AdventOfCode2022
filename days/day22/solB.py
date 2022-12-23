from Advent2022.helpers.parse_input import *

# Get input
arr = [list(line[:-1]) for line in open(get_input_path(22))]
instr = ''.join(arr[-1])
arr = arr[:-2]

#Init x and y
px = 0
py = 0

while arr[0][px] == ' ':
    px += 1

#Find Maxes
MAX_X = 0
MAX_Y = len(arr)

for line in arr:
    MAX_X = max(MAX_Y, len(line))

#Pad arrays
for line in arr:
    while len(line) < MAX_X:
        line.append(' ')

#Set combines
# (D, X, Y)
partners = {}
new_partners = {}
for i in range(0, 50):
    partners[(2, 50, 49 - i)]   = (0, 0, 100 + i)   #Brown
    partners[(2, 50, 50 + i)]   = (1, i, 100)       #Green
    partners[(3, 50 + i, 0)]    = (0, 0, 150 + i)   #Pink
    partners[(3, 100 + i, 0)]   = (3, 0 + i, 199)   #Blue
    partners[(0, 149, 49 - i)]  = (2, 99, 100 + i) #Grey
    partners[(1, 100 + i, 49)]  = (2, 99, 50 + i)   #Bague
    partners[(0, 49, 150 + i)]  = (3, 50 + i, 149)  #Red

for k1, k2, k3 in partners.keys():
    v1, v2, v3 = partners[(k1, k2, k3)]
    new_partners[((v1 + 2) % 4, v2, v3)] = ((k1 + 2) % 4, k2, k3)

partners.update(new_partners)


dpx = [1, 0, -1, 0]
dpy = [0, 1, 0, -1]

i_pointer = 0
direction = 0

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

    return int(instr[x:i_pointer])

def print_arr():
        arr[py][px] = 'X'
        for line in arr:
            for char in line:
                print(char, end='')
            print()
        arr[py][px] = ' '
        print("D: ", direction)
        print("X: ", px)
        print("Y: ", py)
    

def step():

    global px
    global py
    global direction

    print("Position: ", px, py, "Direction: ", direction)

    MAX_X = len(arr[py])

    nx = px
    ny = py
    nd = direction
    
    nx = (nx + dpx[nd])
    ny = (ny + dpy[nd])

    #print("Pre: ", nx, ny)
    if nx < 0 or ny < 0 or nx >= MAX_X or ny >= MAX_Y or arr[ny][nx] == ' ':
        nd, nx, ny = partners[(direction, px, py)]

    if arr[ny][nx] == '#':
        return
    elif arr[ny][nx] == '.':
        py = ny
        px = nx
        direction = nd
        return
    else:
        print(direction, px, py)
        print(nd, nx, ny)
        assert(False)


print(len(arr))
print(arr[-1])

while(i_pointer < len(instr)):
    num_steps = read_instruction(i_pointer)
    for _ in range(num_steps):
        step()

print(px, py, direction)
print(1000 * (py + 1) + 4 * (px + 1) + direction)


