from collections import defaultdict, Counter

from utils import get_file_location

# data load
with open(get_file_location(day=10)) as f:
    data = list(set([int(x) for x in f.read().split('\n')]))

# part 1
i, differences, look_ahead = 0, defaultdict(int), 3
for x in data:
    if x in range(i, i + look_ahead+1):
        differences[x-i] += 1
    i = x
print(differences[1] * (differences[3]+1)) # 2470

# part 2
counter_dict = Counter((0,))
for i, row in enumerate(data):
    counter_dict[row] = sum([counter_dict[y] for y in range(row-look_ahead, row) if y in data or y == 0])
print(counter_dict[data[-1]]) # 1973822685184