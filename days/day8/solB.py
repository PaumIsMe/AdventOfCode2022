from Advent2022.helpers.parse_input import *

def scenic_score(arr, tree_i, tree_j):
    tree_height = arr[tree_i][tree_j]

    view_scores = [0, 0, 0, 0]
    
    #Row Forward
    for i in range (tree_i + 1, len(arr)):
        view_scores[0] = i - tree_i
        if arr[i][tree_j] >= tree_height:
            break

    #Row Backward
    for i in range (tree_i - 1, -1, -1):
        view_scores[1] = tree_i - i
        if arr[i][tree_j] >= tree_height:
            break

    #Col Forward
    for j in range (tree_j + 1, len(arr[0])):
        view_scores[2] = j - tree_j
        if arr[tree_i][j] >= tree_height:
            break

    #Col Backwards
    for j in range (tree_j -1 , -1, -1):
        view_scores[3] = tree_j - j
        if arr[tree_i][j] >= tree_height:
            break

    return view_scores[0] * view_scores[1] * view_scores[2] * view_scores[3]

input_arr = parse_input(8)

two_dim_arr = [[int(c) for c in line] for line in input_arr]

max_scenic_score = 0

for i in range(len(two_dim_arr)):
    for j in range(len(two_dim_arr[i])):
        max_scenic_score = max(max_scenic_score, scenic_score(two_dim_arr, i, j))

print(max_scenic_score)