from collections import defaultdict

from utils import get_file_location

# data load
with open(get_file_location(day=10)) as f:
    data = [int(x) for x in f.read().split('\n')]
data = list(set(data))

# part 1
i, differences = 0, defaultdict(int)
look_ahead = 3
for x in set(data):
    if x in range(i, i + look_ahead+1):
        differences[x-i] += 1
    i = x
differences[3]+=1
print(differences[1] * differences[3]) # 2470

# part 2
counter_dict = defaultdict(int)
counter_dict[0] = 1
for i, row in enumerate(data):
    counter_dict[row] = sum([counter_dict[y] for y in range(row-3, row) if y in data or y == 0])
print(counter_dict[data[-1]]) # 1973822685184