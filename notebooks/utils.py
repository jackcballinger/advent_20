from os.path import join, dirname
from pathlib import Path

def get_file_location(day):
    p = Path(__file__).parent.parent
    return p / 'input_data' / ('day_' + str(day) + '_puzzle_input.txt')
