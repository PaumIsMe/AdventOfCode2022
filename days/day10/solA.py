from Advent2022.helpers.parse_input import *

input_arr = parse_input(10)

c = 1
t = 0
v = 1

for line in input_arr:   
    c += 1
    if (c % 40 == 20):
        t += c * v
    
    if (line[0] == 'a'):
        c += 1
        v += int(line.split(" ")[1])
        if (c % 40 == 20):
            t += c * v

print(t)

