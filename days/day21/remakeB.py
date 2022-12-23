from Advent2022.helpers.parse_input import *

input_arr = parse_input(21)

say = {}

for line in input_arr:
    k, v = line.split(': ')
    say[k] = int(v) if v.isdigit() or k =='humn' else v

# Part B only
say['humn'] = 1j
for char in ['*', '-', '+', '/']:
    say['root'] = say['root'].replace(char, '-')

def find_val(idx):

    v = say[idx]

    if type(v) == int or type(v) == complex:
        return v

    m1, op, m2 = v.strip().split(' ')
    return eval(f'{find_val(m1)} {op} {find_val(m2)}')

answer = find_val('root')

print(answer.real / answer.imag)