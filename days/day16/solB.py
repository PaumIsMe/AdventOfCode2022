from Advent2022.helpers.parse_input import *
import numpy as np
from functools import cache

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

@cache
def solve(score, minutes_left, remaining_valves, player_valve_idx, elephant_valve_idx, player_arrival, elephant_arrival):

    global best_found
   
    #Check if we're out of time
    if minutes_left <= 0 :
        best_found = max(best_found, score)
        return
  
    player_valve = valves[player_valve_idx]
    elephant_valve = valves[elephant_valve_idx]
    player_has_arrived = player_arrival == minutes_left
    elephant_has_arrived = elephant_arrival == minutes_left
    
    #Always flip valve (if we didn't plan on flipping it we'd have gone to a different valve)
    if player_has_arrived:
        score += (minutes_left - 1) * player_valve.flow
    
    if elephant_has_arrived:
        score += (minutes_left - 1) * elephant_valve.flow

    #print(score, minutes_left, "P:", player_valve_idx, "E:", elephant_valve_idx, remaining_valves)

    #Check if we're done with all nodes
    if len(remaining_valves) == 0:

        if player_arrival >= minutes_left and elephant_arrival >= minutes_left:
            print("AAA")
            best_found = max(best_found, score)
            #print(best_found)
            return
        elif player_arrival >= minutes_left:
            solve(score, elephant_arrival, remaining_valves, player_valve_idx, elephant_valve_idx, player_arrival, elephant_arrival)
        else:
            solve(score, player_arrival, remaining_valves, player_valve_idx, elephant_valve_idx, player_arrival, elephant_arrival)
    
    minutes_left -= 1
    remaining_valves = remaining_valves.copy()



    # Try without this, might need, much more awkward to find
    best_possible = score
    if not elephant_has_arrived:
        best_possible += max(0, elephant_valve.flow * (elephant_arrival - 1))
    if not player_has_arrived:
        best_possible += max(0, player_valve.flow * (player_arrival - 1))

    for v in remaining_valves:
        v_score = max(player_arrival - player_valve.distance[v] - 2, elephant_arrival - elephant_valve.distance[v] - 2) * valves[v].flow
        if v_score > 0:
            best_possible += v_score
    
    if best_possible <= best_found:
        return

    #Try moving to all other valves
    if player_has_arrived:
        if elephant_has_arrived:
            for x in remaining_valves:
                for y in remaining_valves:
                    if y != x:
                        pa = minutes_left - player_valve.distance[x]
                        ea = minutes_left - elephant_valve.distance[y]
                        solve(score, max(pa, ea), remaining_valves - set([x, y]), x, y, pa, ea)
                        if best_possible <= best_found:
                            return
        else:
            for x in remaining_valves:
                pa = minutes_left - player_valve.distance[x]
                solve(score, max(pa, elephant_arrival), remaining_valves - set([x]), x, elephant_valve_idx, pa, elephant_arrival)
                if best_possible <= best_found:
                    return
    else:
        for y in remaining_valves:
            ea = minutes_left - elephant_valve.distance[y]
            solve(score, max(player_arrival, ea), remaining_valves - set([y]), player_valve_idx, y, player_arrival, ea)
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

    #solve(score, minutes_left, remaining_valves, player_valve_idx, elephant_valve_idx, player_arrival, elephant_arrival)

for v in valves:
    if v != "AA":
        print("Next Attempt...", flush=True)
        solve(0, 27, set(valves.keys()) - set(["AA", v]), "AA", v, 27, 26 - valves["AA"].distance[v])

print(best_found)







