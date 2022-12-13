from Advent2022.helpers.parse_input import *
from functools import cmp_to_key
import numpy as np

def to_list(n):
    if type(n) == list:
        return n
    return [n]

def eval_arrs(x, y):

    if type(x) == int and type(y) == int:
        return np.sign(y - x)

    if type(x) != type(y):
        return eval_arrs(to_list(x), to_list(y))
    
    for i in range(min(len(x), len(y))):
        result = eval_arrs(x[i], y[i])
        if result:
            return result
        
    return np.sign(len(y) - len(x))
            
input_arr = parse_input(13)

input_arr = [eval(line) for line in input_arr if line != '']
input_arr.extend([[[2]], [[6]]])

#print_array(input_arr)

input_arr.sort(key=cmp_to_key(eval_arrs), reverse=True)
print((input_arr.index([[2]]) + 1) * (input_arr.index([[6]]) + 1))
    
#print(sum(valid_idx))