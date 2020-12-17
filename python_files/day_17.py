import numpy as np
from scipy.ndimage.filters import convolve

from utils import get_file_location

# data load
with open(get_file_location(day=17)) as f:
    data = f.read().splitlines()

def iterate(input_grid, neighbour_positions):
    input_grid_padded = np.pad(input_grid, 1)
    neighbours = convolve(
        input_grid_padded,
        neighbour_positions,
        mode='wrap',
        cval=0
    )
    next_grid = np.zeros(input_grid_padded.shape)
    next_grid += (input_grid_padded == 1) & ((neighbours == 2) | (neighbours == 3))
    next_grid += (input_grid_padded == 0) & (neighbours == 3)
    return next_grid

def create_positions_to_check_neighbours(n):
    neighbour_positions = np.ones(tuple(n*[3]))
    if n == 3:
        neighbour_positions[1,1,1] = 0
        return neighbour_positions
    elif n == 4:
        neighbour_positions[1,1,1,1] = 0
        return neighbour_positions

def create_grid(input_data, n):
    x_dim = len(input_data[0])
    y_dim = len(input_data)
    z_dim = 1
    w_dim = 1
    if n == 3:
        return np.zeros((z_dim, y_dim, x_dim))
    elif n == 4:
        return np.zeros((w_dim, z_dim, y_dim, x_dim))

def update_grid(input_data, grid, n):
    z = 0
    for y, line in enumerate(input_data):
        for x, char in enumerate(line):
            put = 0 if char == '.' else 1
            if n == 3:
                grid[z,y,x] = put
            elif n == 4:
                grid[0, z, y, x] = put
    return grid

def number_remaining_active_cubes(input_data, n_dimensions):
    grid = create_grid(input_data, n_dimensions)
    updated_grid = update_grid(input_data, grid, n_dimensions)
    potential_neighbours = create_positions_to_check_neighbours(n_dimensions)
    for i in range(6):
        updated_grid = iterate(updated_grid, neighbour_positions=potential_neighbours)
    return updated_grid

# part 1
print(number_remaining_active_cubes(data, 3).sum()) # 267

# part 2
print(number_remaining_active_cubes(data, 4).sum()) # 1812