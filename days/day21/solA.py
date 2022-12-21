from Advent2022.helpers.parse_input import *

input_arr = parse_input(21)

say = {}
said = {}

#Parse input
for line in input_arr:
    k, v = line.split(':')
    if ' ' in v.strip():
        say[k] = [v, None]
    else:
        say[k] = ['', int(v)]

#Find what a given monkey says
def find_val(idx):
    global say
    v = say[idx]
    if v[1] is not None:
        return v[1]

    m1, op, m2 = v[0].strip().split(' ')
    v[1] = eval(str(find_val(m1)) + ' ' + op + ' ' + str(find_val(m2)))

    return v[1]

print(find_val('root'))
