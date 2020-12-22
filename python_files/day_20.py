from collections import defaultdict
from itertools import chain
import numpy as np

from utils import get_file_location

with open(get_file_location(day=20)) as f:
    data = f.read()

def format_data(input_data):
    return {int(x.split('\n')[0].replace(':','').split(' ')[1]):
            np.array(x.split('\n')[1:]) for x in input_data.split('\n\n')}

def get_edges(formatted_data):
    return {k:
            {'top': v[0],
             'bottom': v[-1],
             'left': ''.join([y[0] for y in v]),
             'right': ''.join([y[-1] for y in v])
            } for k, v in formatted_data.items()}
formatted_data = format_data(data)
data_edges = get_edges(formatted_data)

# part 1
edge_count_dict = defaultdict(list)
all_rows = list(chain(*[[v for v in x.values()] for x in data_edges.values()]))
for k, v in data_edges.items():
    for row in v.values():
        if all_rows.count(row) == 2:
            edge_count_dict[k].append(all_rows.count(row)-1)
        elif all_rows.count(row) == 1:
            edge_count_dict[k].append(all_rows.count(row[::-1])) 
print(np.product([k for k, v in edge_count_dict.items() if sum(v) == 2])) # 174206308298779