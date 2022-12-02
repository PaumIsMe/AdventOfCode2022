def parse_input(day_number):
    file_path = "../../inputs/day" + str(day_number) + "/input.txt"
    text_file = open(file_path, "r")
    arr = text_file.read().split('\n')
    return arr

def convert_to_int(arr):
    for idx, line in enumerate(arr):
        try:
            arr[idx] = int(line)
        except:
            arr[idx] = None
    return arr

def split_array(arr):
    arr = [line.split(' ') for line in arr]
    return arr