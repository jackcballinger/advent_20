import itertools
import numpy as np

# data load
with open('puzzle_input.txt') as f:
    data = [int(x) for x in f.read().split('\n')]
    
# part 1
print(np.prod(list(filter(lambda x: sum(x)==2020, itertools.combinations(data,2)))))

# part 2
print(np.prod(list(filter(lambda x: sum(x)==2020, itertools.combinations(data,3)))))
