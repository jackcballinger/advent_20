import numpy as np

from utils import get_file_location

# data load
with open(get_file_location(day=5)) as f:
    data = f.read().split('\n')
    
class SeatFinder:
    def __init__(self, row):
        self.row = row
        self.lower_row_bound, self.lower_seat_bound = 0, 0
        self.upper_row_bound = 127
        self.upper_seat_bound = 7
    
    def _midpoint(self, lower_bound, upper_bound):
        return lower_bound + ((upper_bound - lower_bound)/2)
    
    def _find_row(self):
        while True:
            for cmd in self.row:
                if cmd == 'F':
                    self.upper_row_bound = np.floor(self._midpoint(self.lower_row_bound, self.upper_row_bound))
                elif cmd == 'B':
                    self.lower_row_bound = np.ceil(self._midpoint(self.lower_row_bound, self.upper_row_bound))
            if self.lower_row_bound == self.upper_row_bound:
                break
        assert self.lower_row_bound == self.upper_row_bound
        return self.lower_row_bound
    
    def _find_seat(self):
        while True:
            for cmd in self.row[-3:]:
                if cmd == 'L':
                    self.upper_seat_bound = np.floor(self._midpoint(self.lower_seat_bound, self.upper_seat_bound))
                elif cmd == 'R':
                    self.lower_seat_bound = np.ceil(self._midpoint(self.lower_seat_bound, self.upper_seat_bound))
            if self.lower_seat_bound == self.upper_seat_bound:
                break
        assert self.lower_seat_bound == self.upper_seat_bound
        return self.lower_seat_bound
    
    def find_seat_id(self):
        row_number = self._find_row()
        seat_number = self._find_seat()
        return (row_number * 8) + seat_number
    
# part 1
seat_ids = [SeatFinder(row).find_seat_id() for row in data]
print(max(seat_ids))

# part 2
print(set(range(int(min(seat_ids)),int(max(seat_ids)))) - set(seat_ids))
