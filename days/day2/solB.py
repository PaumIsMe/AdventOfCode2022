from Advent2022.helpers.parse_input import *

input_arr = split_array(parse_input(2))

print(input_arr)

value_dick = {"Rock": 0, "Paper": 1, "Scissors": 2}
opponent_dick= {"A": "Rock", "B": "Paper", "C": "Scissors"}
outcome_dick = {"X": "Lose", "Y": "Draw", "Z": "Win"}
points_dick = {"Win": 6, "Draw": 3, "Lose": 0}
points_adjustment_dick = {"Draw": 0, "Win": 1, "Lose": 2}

total_points = 0

try:
    for [opponent_move, player_move] in input_arr:
        decision = outcome_dick[player_move]
        opponent_select = opponent_dick[opponent_move]
        total_points += points_dick[decision]
        total_points += (( value_dick[opponent_select] + points_adjustment_dick[decision] ) % 3) + 1
except:
    print("Bad structure")

print(total_points)
