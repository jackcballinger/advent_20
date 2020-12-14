from collections import Counter
import re
import itertools

from utils import get_file_location

# data load
with open(get_file_location(day=14)) as f:
    data = f.read()

def format_data(input_data):
    input_data_formatted = ['mask' + x for x in input_data.split('mask')[1:]]
    input_data_formatted = [[y for y in x.split('\n') if y != ''] for x in input_data_formatted]
    input_data_formatted = [[(y.split('=')[0].strip(), y.split('=')[1].strip()) for y in x] for x in input_data_formatted]
    return input_data_formatted

def apply_bitmask_v1(input_data):
    formatted_input_data = format_data(input_data)
    program_values = {}
    for program in formatted_input_data:
        program_mask = program[0][1]
        program_instructions = [(x[0], int(x[1])) for x in program[1:]]
        new_program = {}
        for line in program_instructions:
            new_line = ''
            for digit, mask_digit in zip(bin(line[1])[2:].zfill(36), program_mask):
                if mask_digit == 'X':
                    new_line += digit
                else:
                    new_line += mask_digit
            new_program.update({line[0]:new_line})
        program_values.update(new_program)
    return sum([int(v,2) for v in program_values.values()])

def apply_bitmask_v2(input_data):
    program_values = []
    for program in input_data:
        program_mask = program[0][1]
        program_instructions = [(int(re.search(re.compile(r'\[([0-9]+)\]'), x[0]).group(1)),
                                 int(x[1])) for x in program[1:]]
        new_program = []
        for line in program_instructions:
            new_line = ''
            memory_address = bin(line[0])[2:].zfill(36)
            for digit, mask_digit in zip(memory_address, program_mask):
                if mask_digit == 'X' or digit == '0':
                    new_line += mask_digit
                else:
                    new_line += digit
            new_program.append((line[0],(new_line, line[1])))
        program_values.append(new_program)
    return program_values

def get_combinations(program_values):
    combination_values = {}
    for program_value in program_values:
        for program_mask in program_value:
            program_mask_formatted = str(program_mask[1][0])
            x_positions = [i for i in range(len(program_mask_formatted)) if program_mask_formatted.startswith('X', i)]
            for combination in list(map(list, itertools.product(['0', '1'], repeat=program_mask_formatted.count('X')))):
                new_value = [char for char in program_mask_formatted]
                for i, index_val in enumerate(x_positions):
                    new_value[index_val] = combination[i]
                combination_values.update({int(''.join(new_value),2): (''.join(new_value),program_mask[1][1])})
    return combination_values

def get_values_left_in_memory(input_data):
    formatted_input_data = format_data(input_data)
    program_values = apply_bitmask_v2(formatted_input_data)
    combination_values = get_combinations(program_values)

    counter = Counter()
    for k, v in combination_values.items():
        counter[v[1]] += 1
    
    return sum([k*v for k,v in counter.items()])

# part 1
print(apply_bitmask_v1(data)) # 12610010960049

# part 2
print(get_values_left_in_memory(data)) # 3608464522781