from Advent2022.helpers.parse_input import *
import re

tl_br = set()
bl_tr = set()

for line in parse_input(15):
    sx, sy, bx, by = map(int, re.compile(r"-?\d+").findall(line))
    d = abs(sx - bx) + abs(sy - by)
    for side in [-d, d]:
        tl_br.add(sy + sx + side)
        bl_tr.add(sy - sx + side)

f = []
for line_set in (tl_br, bl_tr):
    for i in line_set:
        if i + 2 in line_set:
            f.append(i + 1)

print(4_000_000 * (f[0] - f[1]) // 2 + (f[0] + f[1]) // 2)