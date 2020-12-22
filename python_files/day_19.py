from itertools import chain, product
import re

from utils import get_file_location

with open(get_file_location(day=19)) as f:
    data = f.read()

def format_data(input_data):
    rules = {int(x.split(':')[0]):x.split(':')[1].strip().replace('"','') for x in input_data.split('\n\n')[0].splitlines()}
    rules = {k: [[y if y == 'a' or y == 'b' else int(y) for y in x.strip().split(' ')] for x in v.split('|')] for k, v in rules.items()}
    messages = input_data.split('\n\n')[1].splitlines()
    return rules, messages

rules, messages = format_data(data)
alpha_dict = updated_replacement_dict = {k:v for k, v in rules.items() if 'a' in list(chain(*v)) or 'b' in list(chain(*v))}
new_rules = rules.copy()

# part 1
while True:
    replacement_dict = {key: [
        [int(y) for y in x]
        for x in value]
        for key, value in {k:v for k, v in new_rules.items() if set(list(chain(*v))).intersection(set(list(alpha_dict.keys()))) == set(list(chain(*v)))
        }.items()}
    updated_replacement_dict = {k: list(chain(*[[''.join(list(chain(*list(x)))) for x in list(
        product(*[alpha_dict[combination[i]] for i in range(len(combination))])
    )] for combination in v])) for k, v in replacement_dict.items()}
    alpha_dict.update(updated_replacement_dict)
    new_rules = {k: v for k, v in new_rules.items() if k not in alpha_dict}
    if not new_rules:
        break
print(len([message for message in messages if message in alpha_dict[0]])) # 250