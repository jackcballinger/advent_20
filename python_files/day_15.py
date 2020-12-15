from collections import defaultdict
import numpy as np

from utils import get_file_location

# data load
with open(get_file_location(day=15)) as f:
    data = [int(x) for x in f.read().split(',')]

# part 1
spoken_numbers_array = data.copy()
while len(spoken_numbers_array) < 2020 + 1:
    current_number = spoken_numbers_array[-1]
    if current_number not in spoken_numbers_array[:-1]:
        spoken_numbers_array = np.append(spoken_numbers_array, 0)
    else:
        difference = len(spoken_numbers_array) - np.where(spoken_numbers_array == current_number)[0][-2]-1
        spoken_numbers_array = np.append(spoken_numbers_array, difference)
print(current_number)

# part 2
spoken_numbers_array = data.copy()
index_dict = {n:i for i,n in enumerate(spoken_numbers_array[:-1])}
last_seen_dict = defaultdict(lambda: turn, index_dict)
current_number = spoken_numbers_array[-1]
for turn in range(len(spoken_numbers_array) - 1, 30000000 - 1):
    last_seen_dict[current_number], current_number = turn, turn - last_seen_dict[current_number]
print(current_number) # 129262

# part 1 method takes way too long for part 2, so had to use a different method - try iterating over turn numbers
# and keeping track of the last time a specific number turned up