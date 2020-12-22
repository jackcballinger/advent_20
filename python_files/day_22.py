from utils import get_file_location

with open(get_file_location(day=22)) as f:
    data = f.read()

def format_data(input_data):
    return {x.split(':')[0]: [int(y) for y in x.split(':')[1].splitlines()[1:]] for x in input_data.split('\n\n')}

def determine_result(input_dict, cards_dict):
    winner = 'Player 1' if input_dict['Player 1'] > input_dict['Player 2'] else 'Player 2'
    cards_dict_new = {k: v[1:] for k, v in cards_dict.items()}
    cards_dict_new[winner].extend(list(input_dict.values())) if winner == 'Player 1' else cards_dict_new[winner].extend(list(input_dict.values())[::-1])
    return cards_dict_new

def get_winner(input_data):
    cards_dict = input_data
    while True:
        current_cards = {k:v[0] for k, v in cards_dict.items()}
        updated_cards_dict = determine_result(current_cards, cards_dict)
        if not updated_cards_dict['Player 1'] or not updated_cards_dict['Player 2']:
            break
        cards_dict = updated_cards_dict
    winner_score = sum([x*((updated_cards_dict['Player 2'][::-1].index(x))+1) for x in updated_cards_dict['Player 2'][::-1]]) if not updated_cards_dict['Player 1'] else sum([x*((updated_cards_dict['Player 1'][::-1].index(x))+1) for x in updated_cards_dict['Player 1'][::-1]])
    return winner_score

winner_score = get_winner(format_data(data))
print(winner_score)