import re

# data load
with open('puzzle_input.txt') as f:
    data = [(x.split(':')[0].split(' ')[0], x.split(':')[0].split(' ')[1], x.split(':')[1].strip()) for x in f.read().split('\n')]
    
# part 1
print(len([x for x in data if len(re.findall(x[1], x[2])) in range(int(x[0].split('-')[0]), int(x[0].split('-')[1]) + 1)]))

# part 2
print(len([x for x in data if (x[2][int(x[0].split('-')[0])-1] == x[1]) != (x[2][int(x[0].split('-')[1])-1] == x[1])]))