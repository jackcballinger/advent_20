import itertools

from utils import get_file_location

# data load
with open(get_file_location(day=9)) as f:
    data = [int(x) for x in f.read().split('\n')]
    
class EncodingFixer:
    def __init__(self, input_data, preamble):
        self.input_data = input_data
        self.preamble = preamble
        
    def find_broken_row(self):
        for i, row in enumerate(self.input_data[self.preamble:]):
            if not [x for x in list(itertools.combinations(self.input_data[i:i+self.preamble],2)) if sum(x) == row]:
                return row
    
    def find_contiguous_set(self):
        broken_row = self.find_broken_row()
        for i in range(len(self.input_data)):
            sums = [sum(self.input_data[i:x]) for x in range(len(self.input_data)-i)]
            if broken_row in sums:
                position = sums.index(broken_row)
                return self.input_data[i:position]
            
    def find_encryption_weakness(self):
        contiguous_set = self.find_contiguous_set()
        return min(contiguous_set) + max(contiguous_set)
    
encoding_fixer = EncodingFixer(data, preamble=25)

# part 1
broken_row = encoding_fixer.find_broken_row()
print(broken_row)

# part 2
encryption_weakness = encoding_fixer.find_encryption_weakness()
print(encryption_weakness)