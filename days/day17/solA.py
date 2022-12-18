from Advent2022.helpers.parse_input import *

wind = parse_input(17)[0]
wind = [-1 if i == '<' else 1 for i in wind]

NUM_ROCK_PATTERNS = 5
NUM_WIND_GUSTS = len(wind)
ROCKS_TO_SIM = 2022

rock_patterns = []
rock_patterns.append( {(4, 2), (4, 3), (4, 4), (4, 5)})
rock_patterns.append( {(4, 3), (5, 2), (5, 3), (5, 4), (6, 3)} )
rock_patterns.append( {(4, 2), (4, 3), (4, 4), (5, 4), (6, 4)} )
rock_patterns.append( {(4, 2), (5, 2), (6, 2), (7, 2)})
rock_patterns.append( {(4, 2), (4, 3), (5, 2), (5, 3)})

def sim(n):

    height = 0
    wind_idx = 0
    falling_grid = set([(0, i) for i in range(7)])

    for rock in range(n):

        rock_idx = rock % NUM_ROCK_PATTERNS

        #Spawn in rock
        rock_pattern = rock_patterns[rock_idx]

        coords = []

        for c in rock_pattern:
            coords.append((c[0] + height, c[1]))
        
        #Drop rock
        while (True):
            
            #Wind
            wind_direction = wind[wind_idx]
            wind_idx = (wind_idx + 1) % NUM_WIND_GUSTS
            test_coords = [(c[0], c[1] + wind_direction) for c in coords]
            if not any([c in falling_grid or c[1] < 0 or c[1] >= 7 for c in test_coords]):
                coords = test_coords
                
            #Dropping
            test_coords = [(c[0] - 1, c[1]) for c in coords]
            if not any([c in falling_grid for c in test_coords]):
                coords = test_coords
            else:
                for c in coords:
                    falling_grid.add(c)
                height = max(height, *[c[0] for c in coords])
                
                break
        
    return height

if __name__ == '__main__':
    print("Start sim...")
    print(sim(100000))

    print(1.933 * 1000000000000 / 100000, " seconds =")
    print(1.933 * 1000000000000 / 100000 / 60, " minutes =")
    print(1.933 * 1000000000000 / 100000 / 60 / 60, " hours =")
    print(1.933 * 1000000000000 / 100000 / 60 / 60 / 24, " days =")
    print(1.933 * 1000000000000 / 100000 / 60 / 60 / 24 / 365.25, " years =")
    print(1.933 * 1000000000000 / 100000 / 60 / 60 / 24 / 365.25 / 100, " centuries")

