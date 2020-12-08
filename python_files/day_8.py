import random

from utils import get_file_location

with open(get_file_location(day=8)) as f:
    data = [[x.split(' ')[0], int(x.split(' ')[1])] for x in f.read().split('\n')]
data = list(zip(random.sample(range(0,len(data)), len(data)), data))

# part 1
accumulator = 0
i = 0
used_list = []
while True:
    move = data[i]
    if not move[0] in used_list:
        if move[1][0] == 'jmp':
            i += move[1][1]
        elif move[1][0] == 'acc':
            accumulator += move[1][1]
            i += 1
        elif move[1][0] == 'nop':
            i += 1
        used_list.append(move[0])
    else:
        break
print(accumulator) # 1451

# part 2
def test_for_corruptness(data):
    i = 0
    accumulator = 0
    used_list = []
    while True:
        if i == len(data):
            return False, accumulator
        move = data[i]
        if not move[0] in used_list:
            if move[1][0] == 'jmp':
                i += move[1][1]
            elif move[1][0] == 'acc':
                accumulator += move[1][1]
                i += 1
            elif move[1][0] == 'nop':
                i += 1
            used_list.append(move[0])
        else:
            return True, accumulator


corrupt_lines = []
for line in data:
    if line[1][0] == 'nop':
        line[1][0] = line[1][0].replace('nop','jmp')
        corrupt, accumulator = test_for_corruptness(data)
        if corrupt == False:
            corrupt_lines.append(line)
            print(accumulator)
        line[1][0] = line[1][0].replace('jmp','nop')
    elif line[1][0] == 'jmp':
        line[1][0] = line[1][0].replace('jmp','nop')
        corrupt, accumulator = test_for_corruptness(data)
        if corrupt == False:
            corrupt_lines.append(line)
            print(accumulator)
        line[1][0] = line[1][0].replace('nop','jmp')
print(corrupt_lines) # 1160