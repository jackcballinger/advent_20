from collections import defaultdict, Counter
from itertools import chain, combinations, permutations
import numpy as np

from utils import get_file_location

# data load
with open(get_file_location(day=16)) as f:
    data = f.read()

# data prep
def format_data(input_data):
    valid_ranges_input = {x.split(':')[0]: (range(int(x.split(':')[1].split(' or ')[0].strip().split('-')[0]),
                                            int(x.split(':')[1].split(' or ')[0].strip().split('-')[1])+1),
                                           (range(int(x.split(':')[1].split(' or ')[1].strip().split('-')[0]),
                                            int(x.split(':')[1].split(' or ')[1].strip().split('-')[1])+1))
                                           ) for x in input_data.split('\n\n')[0].split('\n')}
    nearby_tickets_input = {i:[int(y) for y in x.split(',')] for i, x in enumerate(input_data.split('\n\n')[2].split('\n')[1:])}
    your_ticket_input = [int(x) for x in input_data.split('\n\n')[1].split('\n')[1].split(',')]
    return valid_ranges_input, nearby_tickets_input, your_ticket_input

valid_ranges, nearby_tickets, your_ticket = format_data(data)

# part 1
invalid_items = [val for val in list(chain(*list(nearby_tickets.values()))) if all([True if val not in ticket_range else False for ticket_range in list(chain(*list(valid_ranges.values())))])]
print(sum(invalid_items)) # 20058

# part 2
valid_tickets = {k:v for k, v in nearby_tickets.items() if not set(v).intersection(set(invalid_items))}
valid_ticket_values = np.array(list(valid_tickets.values()))

# find all the rows that fit the conditions for each property
col_mapping_dict = defaultdict(str)
for k, v in valid_ranges.items():
    col_mapping_dict[k] = [i for i in range(len(valid_ticket_values[0])) if all(elem in list(chain(*v)) for elem in valid_ticket_values[:,i])]

# find the number of occurances for each column
occurances_dict = {k: v for k, v in sorted(Counter(list(chain(*list(col_mapping_dict.values())))).items(), key=lambda item: item[1])}

seat_positions = {}
for col, col_count in occurances_dict.items():
    seat_positions.update({col:[k for k, v in col_mapping_dict.items() if col in v][0]})
    col_mapping_dict = {k:v for k,v in col_mapping_dict.items() if col not in v}
seat_positions = {k: v for k, v in sorted(seat_positions.items(), key=lambda item: item[0])}
print(np.product([your_ticket[k] for k,v in seat_positions.items() if 'departure' in v])) # 366871907221