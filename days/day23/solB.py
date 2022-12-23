from Advent2022.helpers.parse_input import *
from collections import deque

input_arr = parse_input(23)

e = set()
c = dict()

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
for round in range(10000000):

    #Clear previous considerations
    c = dict()

    #Get all the elves' considerations
    for elf in e:

        #Get possible considerations
        will_consider = []
        for direction in directions:        
            if all([tuple_add(elf, tuple_adapt(direction, i)) not in e for i in [-1, 0, 1]]):
                will_consider.append(tuple_add(elf, direction))
        
        #print(will_consider)

        #Add final consideration
        if will_consider and len(will_consider) < 4:
            final_choice = will_consider[0]
            if final_choice in c.keys():
                c[final_choice] = None
            else:
                c[final_choice] = elf
    
    #Move all elves with non-overlapping considerations
    we_moved_an_elf = False
    for k in c.keys():
        v = c[k]
        if v != None:
            we_moved_an_elf = True
            e.add(k)
            e.remove(v)
    
    if not we_moved_an_elf:
        print(round + 1)
        exit(0)

    #Update direction order
    directions.append(directions.popleft())

print("It never ends...")