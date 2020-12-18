from functools import reduce
import re

from utils import get_file_location

with open(get_file_location(day=18)) as f:
    data = f.read().splitlines()

def operate(a, b):
    assert isinstance(a, int)
    assert isinstance(b, tuple)
    if b[0].strip() == '+':
        return a + int(b[1])
    elif b[0].strip() == '*':
        return a * int(b[1])

def evaluate_additions(input_string):
    new_string = input_string
    while True:
        if '+' not in new_string:
            return new_string
        replacement_dict = dict(zip(
            [''.join([y for y in x]) for x in re.findall(re.compile(r'([0-9]+[\s])([+()]\s)([0-9]+)'), new_string)],
            [str(eval(''.join([y.strip() for y in list(x)]))) for x in re.findall(re.compile(r'([0-9]+[\s])([+()]\s)([0-9]+)'), new_string)]
        ))
        for value, replacement_value in replacement_dict.items():
            new_string = new_string[:new_string.rfind(value)] + new_string[new_string.rfind(value):].replace(value,  replacement_value)
    
def split_string(input_string, addition_first=False):
    if addition_first:
        input_string = evaluate_additions(input_string)
    return [int(input_string.split(' ')[0])] + re.findall(re.compile(r'([+\-\*\/()]\s)([0-9]+)'), input_string)

def evaluate_line(input_line, addition_first=False):
    new_string = input_line
    while True:
        if '(' not in new_string:
            break
        replacement_dict = dict(zip(
            re.findall(re.compile(r'\([^()]*\)'), new_string),
            [str(reduce(operate, split_string(x.replace('(','').replace(')',''), addition_first))) for x in re.findall(re.compile(r'\([^()]*\)'), new_string)]
        ))
        for value, replacement_value in replacement_dict.items():
            new_string = new_string.replace(value, replacement_value)
    return reduce(operate, split_string(new_string, addition_first))

# part 1
print(sum([evaluate_line(line, False) for line in data])) # 1451467526514

# part 2
print(sum([evaluate_line(line, True) for line in data])) # 224973686321527