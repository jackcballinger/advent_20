import re

from utils import get_file_location

# data load
with open(get_file_location(day=7)) as f:
    data = f.read().split('\n')
    
# format_data into dict
data_dict = {
    y.split('bags')[0].strip().replace(' ','_'): [(x.strip().replace('.','').split(' ')[0], '_'.join(x.strip().replace('.','').split(' ')[1:-1])) for x in y.split('contain')[1].strip().split(',')]
    for y in data
}

# part 1
def get_sub_bags(bag):
    sub_bags = new_sub_bags = data_dict[bag].copy()
    for sub_bag in sub_bags:
        if sub_bag[1] != 'other':
            new_sub_bags += data_dict[sub_bag[1]]
        else:
            pass
    return set(new_sub_bags)
print(sum([True if 'shiny_gold' in [x[1] for x in set(get_sub_bags(bag))] else False for bag in data_dict])) # 259

# part 2
# define recursive function to iterate through path
def get_num_bags(bag, bag_multiplier=1):
    if isinstance(bag, str):
        bag = (bag_multiplier, bag)
    n_bags = []
    n_bags.append(int(bag_multiplier))
    for sub_bag in data_dict[bag[1]]:
        if sub_bag[1] in end_points:
            n_bags.append(int(sub_bag[0]) * int(bag_multiplier))
        else:
            n_bags.extend(get_num_bags(sub_bag, int(sub_bag[0]) * int(bag_multiplier)))
    return n_bags

# define bags that contain no further bags, or 'end_points'
end_points = [k for k,v in bag_number_dict.items() if len(v)==1 and v[0][0] == 'no']

print(sum(get_num_bags('shiny_gold'))-1) # 45018
