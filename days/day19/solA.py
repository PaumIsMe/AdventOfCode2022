from Advent2022.helpers.parse_input import *
import re
from functools import cache

input_arr = parse_input(19)

costs = None

ignore_days = {23, 22, 20, 18, 16, 15, 14, 11, 10, 8, 7, 5, 4, 2, 1, 0}
ore_days = {}
clay_days = {21, 19, 17, 12}
ob_days = {13, 9}
geo_days = {6, 3}

@cache
def solve(ore, clay, ob, ore_bot, clay_bot, ob_bot, days):

    if days == 0:
        return 0

    days -= 1

    res = 0

    if ore >= costs[3][0] and ob >= costs[3][1] and days >= 1:
        return days + solve(ore - costs[3][0] + ore_bot, clay + clay_bot, ob - costs[3][1] + ob_bot, ore_bot, clay_bot, ob_bot, days)

    if ore >= costs[2][0] and clay >= costs[2][1] and days >= 3:
        return solve(ore - costs[2][0] + ore_bot, clay - costs[2][1] + clay_bot, ob + ob_bot, ore_bot, clay_bot, ob_bot + 1, days)

    if ore >= costs[1] and days >= 5:
        res = max(res, solve(ore - costs[1] + ore_bot, clay + clay_bot, ob + ob_bot, ore_bot, clay_bot + 1, ob_bot, days))

    if ore >= costs[0] and days >= 7:
        res = max(res, solve(ore - costs[0] + ore_bot, clay + clay_bot, ob + ob_bot, ore_bot + 1, clay_bot, ob_bot, days))
    
    res = max(res, solve(ore + ore_bot, clay + clay_bot, ob + ob_bot, ore_bot, clay_bot, ob_bot, days))
    
    return res

total = 1
parse_ints = re.compile(r"-?\d+")

for i, line in enumerate(input_arr[0:3]):

    costs = [l for l in map(int, parse_ints.findall(line))][1:]
    costs[2] = (costs[2], costs[3])
    costs[3] = (costs[4], costs[5])
    costs = costs[0:4]

    print(costs)

    total *= solve(0, 0, 0, 1, 0, 0, 32)
    solve.cache_clear()

    print(total)
    
    
print(total)

