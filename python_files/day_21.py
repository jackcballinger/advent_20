from itertools import chain
import re

from utils import get_file_location

with open(get_file_location(day=21)) as f:
    data = f.read().splitlines()

test_data = '''mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)'''.splitlines()

def get_allergen_ingredient_mappings(input_data):
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
    return ingredient_list, safe_ingredients

# part 1
ingredient_list, safe_ingredients = get_allergen_ingredient_mappings(data)
print(sum([ingredient_list.count(safe_ingredient) for safe_ingredient in safe_ingredients])) # 2485