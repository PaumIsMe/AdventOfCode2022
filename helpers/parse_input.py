def parse_input(day_number):
    file_path = get_input_path(day_number)
    return [line.strip() for line in open(file_path)]

def get_input_path(day_number):
    return "../../inputs/day" + str(day_number) + "/input.txt"

def convert_to_int(arr):
    for idx, line in enumerate(arr):
        try:
            arr[idx] = int(line)
        except:
            arr[idx] = None
    return arr

def split_array(arr, c):
    arr = [line.split(c) for line in arr]
    return arr

def print_array(arr):
    for line in arr:
        print(line)

def all_unique(str):
    unique_check = set([])
    
    for char in str:
        if char in unique_check:
            return False
        unique_check.add(char)

    return True

