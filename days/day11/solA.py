from Advent2022.helpers.parse_input import *

input_arr = parse_input(11)

class Monkey:
    def __init__(self, items, op, val, mod, t, f):
        self.inspections = 0
        self.items = items
        self.op = op
        self.val = val
        self.mod = mod
        self.t = t
        self.f = f

    def inspect(self, num):
        operand = num if self.val == 'old' else int(self.val)        
        return num * operand if self.op == '*' else num + operand

monkeys = []

for i in range(0, len(input_arr), 7):

    operator, operand = input_arr[i + 2].split(' ')[-2:]
    monkey_arr = list(map(int, input_arr[i + 1].replace(',', '').split(' ')[2:]))
    mod = int(input_arr[i + 3].split(' ')[-1])
    t = int(input_arr[i + 4].split(' ')[-1])
    f = int(input_arr[i + 5].split(' ')[-1])

    monkeys.append(Monkey(monkey_arr, operator, operand, mod, t, f))

for rounds in range(0, 20):

    for m in monkeys:
        for item in m.items:
            m.inspections += 1
            item = m.inspect(item)
            item = item // 3
            if item % m.mod == 0:
                monkeys[m.t].items.append(item)
            else:
                monkeys[m.f].items.append(item)
        m.items = []

num_inspections = [m.inspections for m in monkeys]
num_inspections.sort()
print(num_inspections[-1] * num_inspections[-2])