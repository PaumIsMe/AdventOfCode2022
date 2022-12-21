from Advent2022.helpers.parse_input import *
import copy

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

said = copy.deepcopy(say)

m1, _, m2 = say['root'][0].strip().split(' ')

#Find what a given monkey says
def find_val(idx):
    global say
    v = say[idx]
    if v[1] is not None:
        return v[1]

    m1, op, m2 = v[0].strip().split(' ')
    v[1] = eval(str(find_val(m1)) + ' ' + op + ' ' + str(find_val(m2)))

    return v[1]

#See what values gets the root monkey closest to saying True
def closest_to_zero(r):
    global said
    global say

    found = []

    for i in r:
        said['humn'] = ['', i]
        say = copy.deepcopy(said)
        num1 = find_val(m1)
        say = copy.deepcopy(said)
        num2 = find_val(m2)
        found.append(  (abs(num1 - num2), i)  )

    #print(found)
    return min(found)[0] == 0, min(found)[1]

low = 0
step = 1
high = 10
found = False

check_range = range(low, high + 1, high)

while closest_to_zero(range(low, high + 1, high))[1] == high:
    high *= 10
    step *= 10
    print("We go higher...", flush=True)

while not found:
    print("Narrowing by 80%...", flush=True)
    found, closest = closest_to_zero(range(max(low, 0), high, step))
    low = closest - step
    high = closest + step
    step = (high - low) // 10

print(closest)
