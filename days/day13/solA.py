from Advent2022.helpers.parse_input import *
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

valid_idx = []

for idx in range(0, (len(input_arr) + 1)//3):
    arr1 = eval(input_arr[idx*3])
    arr2 = eval(input_arr[idx*3 + 1])

    if eval_arrs(arr1, arr2) == 1:
        valid_idx.append(idx+1)
    
print(sum(valid_idx))