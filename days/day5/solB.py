from Advent2022.helpers.parse_input import *

NUM_CRATE_STACKS = 9

input_arr = parse_input(5)

crate_stacks = [[] for i in range(NUM_CRATE_STACKS + 1)]

#get initial crate stack

for line in input_arr:

    if line[0] != '[':
        break

    for crate_stack in range(1, NUM_CRATE_STACKS + 1):
        char_idx = (crate_stack * 4) - 3
        letter = line[char_idx]
        print(letter)

        if letter != ' ':
            crate_stacks[crate_stack].insert(0, letter)
print_array(crate_stacks)

#go thru crate movements
for line in input_arr:
    if len(line) > 4 and line[0:4] == "move":

        #parse text
        values_in_line = line.split(' ')
        num_movements = int(values_in_line[1])
        from_crate = int(values_in_line[3])
        to_crate = int(values_in_line[5])

        moved_crates = crate_stacks[from_crate][num_movements * -1 : ]
        crate_stacks[to_crate].extend(moved_crates)
        crate_stacks[from_crate] = crate_stacks[from_crate][:num_movements * -1]

print_array(crate_stacks)

for crate_stack in crate_stacks:
    print(crate_stack[-1] if len(crate_stack) > 0 else " ", end='')

#print(input_arr)
