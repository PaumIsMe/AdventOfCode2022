from Advent2022.helpers.parse_input import *
import numpy as np

class Valve:
    def __init__(self, flow_rate, adjacents):
        self.flow = flow_rate
        self.distance = dict()
        self.partners = set(adjacents)
    
    def __str__(self):
        return f"Known distnaces:\n{self.distance}\nValue:\n{self.flow}\n\n"

best_found = 0
max_flow = 0
valves = dict()

def create_valves_from_input(useless, arr):

    max_flow = 0

    for line in arr:
        words = line.split(' ')
        flow = int(words[4][5:-1])
        max_flow = max(max_flow, flow)
        adj = []
        for v in words[9:]:
            adj.append(v[:2])
        valves[words[1]] = Valve(flow, adj)
        if flow == 0 and words[1] != "AA":
            useless.add(words[1])
    
    return max_flow

def bfs(starting_valve_id : Valve, useless_valves):

    next_nodes = []
    after_nodes = [starting_valve_id]
    seen = set([starting_valve_id])
    num_steps = 0

    while after_nodes:

        next_nodes = after_nodes
        after_nodes = []

        for valve_id in next_nodes:
            
            if valve_id not in useless_valves:
                valves[starting_valve_id].distance[valve_id] = num_steps

            for connection in valves[valve_id].partners:
                if connection not in seen:
                    after_nodes.append(connection)
                    seen.add(connection)
        
        num_steps += 1

def solve(score, minutes_left, remaining_valves, current_valve_idx):

    global best_found
    current_valve = valves[current_valve_idx] 
    
    #Check if we're out of time
    if minutes_left <= 0 :
        best_found = max(best_found, score)
        return
    
    #Always flip valve (if we didn't plan on flipping it we'd have gone to a different valve)
    score += (minutes_left - 1) * current_valve.flow
    remaining_valves = remaining_valves.copy()
    remaining_valves.remove(current_valve_idx)
    minutes_left -= 1

    #DD BB JJ HH EE CC
    #print(score, minutes_left, remaining_valves)

    #Check if we're done with all nodes
    if len(remaining_valves) == 0:
        best_found = max(best_found, score)
        return

    #Find best possible score, done if unwinnable
    best_possible = score
    for v in remaining_valves:
        v_score = (minutes_left - current_valve.distance[v] - 1) * valves[v].flow
        if v_score > 0:
            best_possible += v_score
    
    if best_possible <= best_found:
        return

    #Try moving to all other valves
    for v in remaining_valves - set([current_valve_idx]):
        solve(score, minutes_left - current_valve.distance[v], remaining_valves, v)
        if best_possible <= best_found:
            return
    
    return

useless_valves = set()
input_arr = parse_input(16)

max_flow = create_valves_from_input(useless_valves, input_arr)

for v in valves:
    if v not in useless_valves:
        bfs(v, useless_valves)

for v in useless_valves:
    valves.pop(v)

for v in valves:
    print(v)
    print(valves[v])

solve(0, 31, set(valves.keys()), "AA")

print(best_found)







