import numpy as np
from os.path import abspath, dirname
from os import getcwd
from pathlib import Path

try:
    p = Path(__file__).parent
    file_location = p / 'puzzle_input.txt'
except NameError:
    file_location = 'puzzle_input.txt'


# read in data
with open(file_location) as f:
    data = f.read().split('\n')

# configure data
n = len(data)
new_data = [line+(n*line) for line in data]

# toboggan class
class Toboggan:
    def __init__(self, route):
        self.route = route
        self.x_pos, self.y_pos, self.trees = 0,0,0
        
    def navigate(self, x_step, y_step):
        while True:
            if self.y_pos >= len(self.route):
                break
            if self.route[self.y_pos][self.x_pos] == '#':
                self.trees+=1
            self.x_pos += x_step
            self.y_pos += y_step
        return self.trees

# part 1
print(Toboggan(new_data).navigate(x_step=3, y_step=1))

# part 2
slope_list = [
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2)
]

print(np.prod([Toboggan(new_data).navigate(x_step=slope[0], y_step=slope[1]) for slope in slope_list]))
    