from Advent2022.helpers.parse_input import *

input_arr = parse_input(21)

say = {}

for line in input_arr:
    k, v = line.split(': ')
    say[k] = int(v) if v.isdigit() else v

def find_val(idx):

    v = say[idx]
    if type(v) == int:
        return v

    m1, op, m2 = v.strip().split(' ')
    return eval(f'{find_val(m1)} {op} {find_val(m2)}')

print(find_val('root'))
