from Advent2022.helpers.parse_input import *

input_arr = split_array(parse_input(2), ' ')

print(input_arr)

opponent_dick = {"A": "Rock", "B": "Paper", "C": "Scissors"}
player_dick = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}
value_dick = {"Rock": 1, "Paper": 2, "Scissors": 3}
rock_dick = {"Rock": "Draw", "Paper": "Lose", "Scissors": "Win"}
paper_dick = {"Rock": "Win", "Paper": "Draw", "Scissors": "Lose"}
scissors_dick = {"Rock": "Lose", "Paper": "Win", "Scissors": "Draw"}
outcome_dick = {"Rock": rock_dick, "Paper": paper_dick, "Scissors": scissors_dick}
points_dick = {"Win": 6, "Draw": 3, "Lose": 0}

total_points = 0

try:
    for [opponent_move, player_move] in input_arr:
        player_select = player_dick[player_move]
        opponent_select = opponent_dick[opponent_move]
        total_points += value_dick[player_select]
        total_points += points_dick[outcome_dick[player_select][opponent_select]]
except:
    print("Bad structure")
    
print(total_points)
