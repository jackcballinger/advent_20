import numpy as np

# read in data
with open('puzzle_input.txt') as f:
    data = f.read().split('\n')

# configure input_data
n = len(data)
new_data = [line+(n*line) for line in data]

# part 1
x_pos = 0
y_pos = 0
x_step = 3
y_step = 1
trees = 0
while True:
    if y_pos >= len(new_data):
        break
    if new_data[y_pos][x_pos] == '#':
        trees+=1
    x_pos += x_step
    y_pos += y_step
print(trees)

# part 2
pos_list = [
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2)
]

total_trees = []
for pos in pos_list:
    x_pos = 0
    y_pos = 0
    x_step = pos[0]
    y_step = pos[1]
    trees = 0
    while True:
        if y_pos >= len(new_data):
            break
        if new_data[y_pos][x_pos] == '#':
            trees+=1
        x_pos += x_step
        y_pos += y_step
    total_trees.append(trees)
print(np.prod(total_trees))