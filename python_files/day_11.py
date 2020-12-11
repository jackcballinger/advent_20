import numpy as np

from utils import get_file_location

with open(get_file_location(day=11)) as f:
    data = np.array([[seat for seat in row] for row in f.read().split('\n')])

moves_dict = {
    'up':{'x':0, 'y':-1},
    'up_right':{'x':1, 'y':-1},
    'right':{'x':1,'y':0},
    'down_right':{'x':1,'y':1},
    'down':{'x':0, 'y':1},
    'down_left':{'x':-1,'y':1},
    'left':{'x':-1,'y':0},
    'up_left':{'x':-1,'y':-1}
}

def get_neighbour_seat(x_coord, y_coord, direction, input_data, iterate_search=False):
    y = y_coord + moves_dict[direction]['y']
    x = x_coord + moves_dict[direction]['x']
    while 0 <= y <= len(input_data)-1 and 0 <= x <= len(input_data[0])-1:
        if input_data[y][x] != '.':
            return input_data[y][x]
        if iterate_search:
            y+=moves_dict[direction]['y']
            x+=moves_dict[direction]['x']
        else:
            return None

def get_neighbour_seats(x_coord, y_coord, input_data, iterate_search=False):
    return [val for val in [get_neighbour_seat(x_coord,y_coord,k,input_data, iterate_search) for k in moves_dict.keys()] if val is not None]

def get_equilibrium_seating_plan(iterate_search, occupied_limit, input_data):
    prev_array = input_data.copy()
    new_array = input_data.copy()
    while True:
        for y, row in enumerate(prev_array):
            for x, seat in enumerate(row):
                neighbour_seats = get_neighbour_seats(x,y,prev_array,iterate_search=iterate_search)
                if prev_array[y][x] == 'L' and len(set(neighbour_seats)) == 1 and neighbour_seats[0] == 'L':
                    new_array[y][x] = '#'
                elif prev_array[y][x] == '#' and len([x for x in neighbour_seats if x == '#']) >= occupied_limit:
                    new_array[y][x] = 'L'
        if (prev_array == new_array).all():
            break
        prev_array = new_array.copy()
    return np.count_nonzero(prev_array == '#')

# part 1
print(get_equilibrium_seating_plan(iterate_search=False, occupied_limit=4, input_data=data)) # 2481

# part 2
print(get_equilibrium_seating_plan(iterate_search=True, occupied_limit=5, input_data=data)) # 2227