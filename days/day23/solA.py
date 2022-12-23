from Advent2022.helpers.parse_input import *
from collections import deque

input_arr = parse_input(23)

e = set()
c = dict()

min_x = float('inf')
max_x = -1 * float('inf')
min_y = float('inf')
max_y = -1 * float('inf')

# Set the initial positions of the elves
for i, row in enumerate(input_arr):
    for j, tile in enumerate(row):
        if tile == '#':
            e.add((j, i))

#Set directions to check
directions = deque([(0, -1), (0, 1), (-1, 0), (1, 0)])

#Add 2 tuples
def tuple_add(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

#Adapt tuple based on the secondary coord
def tuple_adapt(dir, i):
    return (dir[0] + i, dir[1]) if dir[0] == 0 else (dir[0], dir[1] + i)
    
#Simulate rounds
for round in range(10):

    #Clear previous considerations
    c = dict()

    #Get all the elves' considerations
    for elf in e:

        #Get possible considerations
        will_consider = []
        for direction in directions:        
            if all([tuple_add(elf, tuple_adapt(direction, i)) not in e for i in [-1, 0, 1]]):
                will_consider.append(tuple_add(elf, direction))

        #Add final consideration
        if will_consider and len(will_consider) < 4:
            final_choice = will_consider[0]
            if final_choice in c.keys():
                c[final_choice] = None
            else:
                c[final_choice] = elf
    
    #Move all elves with non-overlapping considerations
    for k in c.keys():
        v = c[k]
        if v != None:
            e.add(k)
            e.remove(v)

    #Update direction order
    directions.append(directions.popleft())

#Find lowest/largest x/y
for x, y in e:
    min_x = min(x, min_x)
    min_y = min(y, min_y)
    max_x = max(x, max_x)
    max_y = max(y, max_y)

#Calculate rectangle size
print((1 + max_x - min_x) * (1 + max_y - min_y) - len(e))