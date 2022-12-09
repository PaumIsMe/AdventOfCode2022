from Advent2022.helpers.parse_input import *

score = 0

for line in parse_input(2):
    a, b = line.split(' ')
    
    opp = ord(a) - ord("A")
    decision = ord(b) - ord("Y")
    us = (opp + decision) % 3

    if (us - opp) % 3 == 1:
        score += 6
    elif us == opp:
        score += 3
    
    score += us + 1

print(score)
