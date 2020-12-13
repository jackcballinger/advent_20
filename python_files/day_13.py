from utils import get_file_location

with open(get_file_location(day=13)) as f:
    data = f.read().split('\n')

class BusTimetable:
    def __init__(self, input_data):
        self.input_data = input_data
        self.busses, self.reduced_busses, self.earliest_time = self._get_formatted_data()
        self.least_frequent_bus = max([x for x in self.reduced_busses if x != 'x'])
        self.relative_bus_indices = {int(bus): self.busses.index(bus) - self.busses.index(str(self.least_frequent_bus)) for bus in self.busses if bus != 'x'}
        
    def _get_formatted_data(self):
        earliest_time = int(self.input_data[0])
        busses = self.input_data[1].split(',')
        reduced_busses = sorted([int(x) for x in busses if x != 'x'], reverse=True)
        return busses, reduced_busses, earliest_time
    
    def get_earliest_bus(self):
        current_time = self.earliest_time
        while True:
            if any(v == 0 for v in [current_time % bus for bus in self.reduced_busses]):
                bus_id = [bus for bus in self.reduced_busses if current_time % bus == 0].pop()
                return (current_time - self.earliest_time) * bus_id
            current_time += 1
            
    def get_earliest_timestamp(self):
        current_time_stamp = iterator = self.least_frequent_bus
        i = 1
        while True:
            if (current_time_stamp + self.relative_bus_indices[self.reduced_busses[i]]) % self.reduced_busses[i] == 0:
                if i == len(self.reduced_busses)-1:
                    return (current_time_stamp) + min(self.relative_bus_indices.values())
                iterator *= self.reduced_busses[i]
                i+=1
            current_time_stamp += iterator

bus_timetable = BusTimetable(data)

# part 1
print(bus_timetable.get_earliest_bus()) # 104