from Advent2022.helpers.parse_input import *

input_arr = parse_input(8)

two_dim_arr = [[(int(c), False) for c in line] for line in input_arr]

#Rows
for i in range(len(two_dim_arr)): #Coule possibly enumerate?
    row = two_dim_arr[i]

    #Row Forwards
    min_val = -1
    for j in range(len(row)):
        tree = row[j]
        if tree[0] > min_val:
            min_val = tree[0]
            row[j] = (row[j][0], True)

    #Row Backwards
    min_val = -1
    for j in range(len(row) - 1, -1, -1):
        tree = row[j]
        if tree[0] > min_val:
            min_val = tree[0]
            row[j] = (row[j][0], True)

#Columns
for j in range(len(two_dim_arr[0])):

    #Col Forwards
    min_val = -1
    for i in range(len(two_dim_arr)):
        tree = two_dim_arr[i][j]
        if tree[0] > min_val:
            min_val = tree[0]
            two_dim_arr[i][j] = (two_dim_arr[i][j][0], True)

    #Col Backwards
    min_val = -1
    for i in range(len(two_dim_arr) - 1, -1, -1):
        tree = two_dim_arr[i][j]
        if tree[0] > min_val:
            min_val = tree[0]
            two_dim_arr[i][j] = (two_dim_arr[i][j][0], True)

total_seen_trees = 0

for row in two_dim_arr:
    for tree in row:
        if tree[1]:
            total_seen_trees += 1

print(total_seen_trees)

#print_array(two_dim_arr)