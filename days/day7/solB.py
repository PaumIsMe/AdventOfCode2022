from Advent2022.helpers.parse_input import *

class File:
    name = ""
    size = ""

    def __init__(self, n, s):
        self.name = n
        self.size = s

class Directory:

    def __init__(self, p):
        self.parent = p
        self.files = []
        self.subdirectories = []
        self.size = None

    def get_size(self):
        if self.size == None:
            self.size = self.eval_size()
        return self.size

    def eval_size(self):
            running_size = 0
            for sub_d in self.subdirectories:
                running_size += sub_d.eval_size()
            for file in self.files:
                running_size += file
            
            return running_size

def get_all_directory_sizes(d : Directory):
    all_sizes = [d.get_size()]
    for sub_d in d.subdirectories:
        all_sizes.extend(get_all_directory_sizes(sub_d))
    return all_sizes

input_arr = split_array(parse_input(7), ' ')

tree_root = Directory(None)
current_pointer = tree_root

for instruction in input_arr:

    #print(instruction)

    if instruction[0] == '$':

        if instruction[1] == 'cd':

            if instruction[2] == '..':

                #Move back a directory
                current_pointer = current_pointer.parent

            else:

                #Create a new directory (doesn't check if it's already there)
                d = Directory(current_pointer)
                current_pointer.subdirectories.append(d)
                current_pointer = d
                
        
        else:

            #We are doing an ls now, which we will ignore
            pass
    
    else:

        if instruction[0] == 'dir':

            #Ignore directory listings
            pass
        
        else:
            current_pointer.files.append(int(instruction[0]))

#print(tree_root.subdirectories[0].subdirectories)
#print(tree_root.subdirectories[0].files)
all_sizes = get_all_directory_sizes(tree_root)

total_size = tree_root.get_size()
excess_size = total_size - 40000000

canidate = 70000000

for elem in all_sizes:
    if elem > excess_size:
        canidate = min(canidate, elem)

print(canidate)