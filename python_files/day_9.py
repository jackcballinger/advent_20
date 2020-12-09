import itertools

from utils import get_file_location

# data load
with open(get_file_location(day=9)) as f:
    data = [int(x) for x in f.read().split('\n')]
    
class EncodingFixer:
    def __init__(self, input_data, preamble, max_combinations):
        self.input_data = input_data
        self.preamble = preamble
        self.max_combinations = max_combinations
        
    def find_broken_row(self):
        for i, row in enumerate(self.input_data[self.preamble:]):
            if not [x for x in list(itertools.combinations(self.input_data[i:i+self.preamble],2)) if sum(x) == row]:
                return row
    
    def find_correct_combinations(self):
        broken_row = self.find_broken_row()
        for i, row in enumerate(self.input_data[:self.input_data.index(broken_row)]):
            for n_combinations in range(1, self.max_combinations+1):
                for x in itertools.combinations(self.input_data[i:i+n_combinations], n_combinations):
                    if sum(x) == broken_row:
                        return x
    
    def find_encryption_weakness(self):
        correct_combinations = self.find_correct_combinations()
        return max(correct_combinations) + min(correct_combinations)
    
encoding_fixer = EncodingFixer(data, preamble=25, max_combinations=20)

# part 1
broken_row = encoding_fixer.find_broken_row()
print(broken_row)

# part 2
encryption_weakness = encoding_fixer.find_encryption_weakness()
print(encryption_weakness)