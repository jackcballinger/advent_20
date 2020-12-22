from collections import Counter
from itertools import chain
import re

from utils import get_file_location

with open(get_file_location(day=21)) as f:
    data = f.read().splitlines()

def get_safe_ingredients(input_data):
    allergen_ingredient_mapping, ingredient_list = {}, []
    for line in input_data:
        m = re.match("^([\w\s]+) \(contains ([\w\s,]+)\)$", line).groups()
        ingredients = m[0].split(" ")
        allergens = m[1].split(", ")
        for allergen in allergens:
            if allergen not in allergen_ingredient_mapping:
                allergen_ingredient_mapping[allergen] = set(ingredients)
            else:
                allergen_ingredient_mapping[allergen] &= set(ingredients)
        ingredient_list.extend(ingredients)
    safe_ingredients = set(ingredient_list) - set(chain(*allergen_ingredient_mapping.values()))
    return ingredient_list, safe_ingredients, allergen_ingredient_mapping

def get_allergen_food_mapping(input_allergen_ingredient_mapping):
    allergen_count_dict = Counter(list(chain.from_iterable(input_allergen_ingredient_mapping.values())))
    allergen_ingredient_mapping_updated = input_allergen_ingredient_mapping
    food_allergen_mapping = {}
    while True:
        current_allergen = [k for k,v in allergen_count_dict.items() if v == 1][0]
        food_allergen_mapping.update({current_allergen: [k for k, v in allergen_ingredient_mapping_updated.items() if current_allergen in v][0]})
        allergen_ingredient_mapping_updated = {k:v for k, v in input_allergen_ingredient_mapping.items() if k not in food_allergen_mapping.values()}
        if not allergen_ingredient_mapping_updated:
            return food_allergen_mapping
        allergen_count_dict = Counter(list(chain.from_iterable(allergen_ingredient_mapping_updated.values())))

ingredient_list, safe_ingredients, allergen_ingredient_mapping = get_safe_ingredients(data)

# part 1
print(sum([ingredient_list.count(safe_ingredient) for safe_ingredient in safe_ingredients])) # 2485

# part 2
print(','.join([x[0] for x in sorted(get_allergen_food_mapping(allergen_ingredient_mapping).items(), key=lambda item: item[1])])) # bqkndvb,zmb,bmrmhm,snhrpv,vflms,bqtvr,qzkjrtl,rkkrx