from Advent2022.helpers.parse_input import *

cals = [0]

for l in parse_input(1):
    if l == "":
        cals.append(0)
    else:
        cals[-1] += int(l)

cals.sort()
print(sum(cals[-3:]))