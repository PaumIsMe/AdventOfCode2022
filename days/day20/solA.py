from Advent2022.helpers.parse_input import *

input_arr = parse_input(20)
arr = []
start_search = 0

for i, num in enumerate(input_arr):
    arr.append((i, int(num)))

for idx in range(len(arr)):

    #print([x[1] for x in arr])

    for i in range(len(arr)):
        start_search = i
        if arr[start_search][0] == idx:
            break
    else:
        print(idx, "Didn't break!!")
    
    elem_to_remove = arr[start_search]
    spots_moved = elem_to_remove[1] % (len(arr) - 1)
    new_location = (spots_moved + start_search)
    if new_location >= len(arr):
        new_location = (new_location + 1) % len(arr)

    arr.remove(elem_to_remove)
    if new_location == 0:
        arr.append(elem_to_remove)
    else:
        arr.insert(new_location, elem_to_remove)

    start_search += 1

    #print(start_search)

output_arr =  [x[1] for x in arr] 
sum = 0

zero_idx = output_arr.index(0)
for num in (1000, 2000, 3000):
    idx = (zero_idx + num) % len(output_arr)
    sum += output_arr[idx]
    print(output_arr[idx])

print(sum)



