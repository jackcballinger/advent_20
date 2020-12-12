from utils import get_file_location

with open(get_file_location(day=12)) as f:
    data = [(x[0],int(x[1:])) for x in f.read().split('\n')]

def transform_waypoint(quantity, waypoint, instruction):
    if instruction == 'R':
        multiplier = 1
    elif instruction == 'L':
        multiplier = -1
    if quantity == 90:
        return (multiplier * waypoint[1], multiplier * -waypoint[0])
    if quantity == 180:
        return (-waypoint[0], -waypoint[1])
    if quantity == 270:
        return (multiplier * -waypoint[1], multiplier * waypoint[0])
    return waypoint

# part 1
move_dict = {
    360: {'x':0, 'y':1},
    90: {'x':1, 'y':0},
    180: {'x':0, 'y':-1},
    270: {'x':-1, 'y':0},
    0: {'x':0, 'y':1}
}

direction_dict = {
    'N': {'x':0, 'y':1},
    'E': {'x':1, 'y':0},
    'S': {'x':0, 'y':-1},
    'W': {'x':-1, 'y':0}
}

turn_dict = {
    'L': -1,
    'R': +1
}

old_coords, new_coords = (0,0), (0,0)
old_direction, new_direction = 90, 90
for row in data:
    instruction = row[0]
    quantity = row[1]
    if instruction == 'F':
        x_new = old_coords[0] + move_dict[old_direction]['x'] * quantity
        y_new = old_coords[1] + move_dict[old_direction]['y'] * quantity
        new_coords = (x_new,y_new)
    elif instruction in ['N','E','S','W']:
        x_new = old_coords[0] + direction_dict[instruction]['x'] * quantity
        y_new = old_coords[1] + direction_dict[instruction]['y'] * quantity
        new_coords = (x_new,y_new)
    elif instruction in ['R','L']:
        new_direction = old_direction + turn_dict[instruction] * quantity
        if new_direction > 360:
            new_direction -= 360
        elif new_direction < 0:
            new_direction += 360
    old_coords = new_coords
    old_direction = new_direction

print(abs(old_coords[0])+abs(old_coords[1])) # 1441

# part 2
old_coords, new_coords = (0,0), (0,0)
old_waypoint, new_waypoint = (10,1), (10,1)
for row in data:
    instruction = row[0]
    quantity = row[1]
    if instruction == 'F':
        x_new = old_coords[0] + (quantity * old_waypoint[0])
        y_new = old_coords[1] + (quantity * old_waypoint[1])
        new_coords = (x_new,y_new)
    elif instruction in ['N','E','S','W']:
        new_waypoint_x = old_waypoint[0] + direction_dict[instruction]['x'] * quantity
        new_waypoint_y = old_waypoint[1] + direction_dict[instruction]['y'] * quantity
        new_waypoint = (new_waypoint_x, new_waypoint_y)
    elif instruction in ['R','L']:
        new_waypoint = transform_waypoint(quantity, old_waypoint, instruction)

    old_coords = new_coords
    old_waypoint = new_waypoint
print(abs(old_coords[0])+abs(old_coords[1])) # 61616