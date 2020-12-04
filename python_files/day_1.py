import itertools
import numpy as np

from utils import get_file_location

# data_load
with open(get_file_location(day=1)) as f:
    data = [int(x) for x in f.read().split('\n')]
    
# part 1
print(np.prod(list(filter(lambda x: sum(x)==2020, itertools.combinations(data,2)))))

# part 2
print(np.prod(list(filter(lambda x: sum(x)==2020, itertools.combinations(data,3)))))
