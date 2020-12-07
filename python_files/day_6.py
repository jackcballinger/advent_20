from itertools import chain

with open('day_6_puzzle_input.txt') as f:
    data = [x.split('\n') for x in f.read().split('\n\n')]

# part 1
print(sum([len(set(''.join([y for y in x]))) for x in data]))

# part 2
passengers = []
for row in data:
    result = set(row[0])
    for x in row[1:]:
        result.intersection_update(x)
    passengers.append(len(result))
print(sum(passengers))
