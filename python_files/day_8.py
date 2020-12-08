import random

from utils import get_file_location

with open(get_file_location(day=8)) as f:
    data = [[x.split(' ')[0], int(x.split(' ')[1])] for x in f.read().split('\n')]
# data = list(zip(random.sample(range(0,len(data)), len(data)), data))

with open(get_file_location(day=8)) as f:
    data = [[x.split(' ')[0], int(x.split(' ')[1])] for x in f.read().split('\n')]

class CorruptnessFinder:
    def __init__(self, data):
        self.data = data
        self.iterator = 0
        self.accumulator = 0
        self.used_list, self.corrupt_moves = [],[]
        self.corrupt_flag = True
        
    def _parse_move(self, move):
        return move[0], move[1]
        
    def _execute_action(self, move):
        move_action, move_quantity = self._parse_move(move)
        if move_action == 'jmp':
            self.iterator += move_quantity
        elif move_action == 'acc':
            self.accumulator += move_quantity
            self.iterator += 1
        elif move_action == 'nop':
            self.iterator += 1
        
    def _test_program_for_corruptness(self):
        while self.corrupt_flag:
            # set corrupt flag to False if we are at the last line of code, thus breaking while loop
            self.corrupt_flag = not self.iterator == len(self.data)
            move = self.data[self.iterator]
            if not self.iterator in self.used_list:
                self.used_list.append(self.iterator)              
                self._execute_action(move)
            else:
                # at this point, we know the file is corrupt, and we don't want to enter into the infinite loop,
                # so break
                break
            
    def _replace_move(self, move, replacement_dict):
        move_action, _ = self._parse_move(move)
        return move_action if move_action not in replacement_dict else replacement_dict[move_action]
                   
        
    def get_accumulator_for_corrupt_program(self):
        self._test_program_for_corruptness()
        return self.accumulator

    def fix_program(self):
        corrupt_lines = []
        for move in self.data:
            if move[0] == 'nop':
                move[0] = move[0].replace('nop','jmp')
                self._test_program_for_corruptness()
                if self.corrupt_flag == False:
                    corrupt_lines.append(move)
                move[0] = move[0].replace('jmp','nop')
            elif move[0] == 'jmp':
                move[0] = move[0].replace('jmp','nop')
                self._test_program_for_corruptness()
                if self.corrupt_flag == False:
                    corrupt_lines.append(move)
                move[0] = move[0].replace('nop','jmp')
        return corrupt_lines
                    
corruptness_finder = CorruptnessFinder(data)        

corrupt_moves = corruptness_finder.fix_program()
pass