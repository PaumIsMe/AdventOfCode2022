from Advent2022.helpers.parse_input import *

sum = 0

for line in parse_input(3):

    s1 = line[:len(line)//2]
    s2 = line[len(line)//2:]

    val = list(set(s1) & set(s2))[0]
    val = ord(val)

    if val >= ord("a"):
        sum += val - ord("a") + 1
    else:
        sum += val - ord("A") + 26 + 1
    
print(sum)