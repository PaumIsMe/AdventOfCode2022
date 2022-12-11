from Advent2022.helpers.parse_input import *

def do_it(x):
    print(x(0))
    print(n)


f1 = lambda x: x + int(n)
f2 = lambda x: x + n


n = 5

do_it(f1)
do_it(f2)