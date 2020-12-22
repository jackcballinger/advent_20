from utils import get_file_location

with open(get_file_location(day=22)) as f:
    data = f.read()

def format_data(input_data):
    return {x.split(':')[0]: [int(y) for y in x.split(':')[1].splitlines()[1:]] for x in input_data.split('\n\n')}

def determine_result(input_dict, cards_dict, winner_given=None):
    if winner_given:
        winner = winner_given
    else:
        winner = 'Player 1' if input_dict['Player 1'] > input_dict['Player 2'] else 'Player 2'
    cards_dict_new = {k: v[1:] for k, v in cards_dict.items()}
    cards_dict_new[winner].extend(list(input_dict.values())) if winner == 'Player 1' else cards_dict_new[winner].extend(list(input_dict.values())[::-1])
    return cards_dict_new

def play_game(input_data, recursion=False):
    previous_cards, updated_cards_dict = [], {}
    while True:
        current_cards = {k:v[0] for k, v in input_data.items()}
        if input_data not in previous_cards:
            previous_cards.append(input_data)
        else:
            return updated_cards_dict, 'Player 1'
        if ((len(input_data['Player 1']) - 1 >= current_cards['Player 1']) and (len(input_data['Player 2']) - 1 >= current_cards['Player 2'])) and recursion:
            game_result = play_game({k: v[1:current_cards[k]+1] for k, v in input_data.items()})
            if game_result[1]:
                updated_cards_dict = determine_result(current_cards, input_data, game_result[1])
            else:
                updated_cards_dict = determine_result(current_cards, input_data, 'Player 1' if not game_result[0]['Player 2'] else 'Player 2')
        else:
            updated_cards_dict = determine_result(current_cards, input_data)
        if not updated_cards_dict['Player 1'] or not updated_cards_dict['Player 2']:
            return updated_cards_dict, None
        input_data = updated_cards_dict

def calculate_winner_score(final_cards_dict, winner=None):
    if winner == None:
        return sum([x*((final_cards_dict['Player 2'][::-1].index(x))+1) for x in final_cards_dict['Player 2'][::-1]]) if not final_cards_dict['Player 1'] else sum([x*((final_cards_dict['Player 1'][::-1].index(x))+1) for x in final_cards_dict['Player 1'][::-1]])
    elif winner == 'Player 1':
        return sum([x*((final_cards_dict['Player 1'][::-1].index(x))+1) for x in final_cards_dict['Player 1'][::-1]])

# part 1
final_game_state, _ = play_game(format_data(data))
print(calculate_winner_score(final_game_state)) # 34324

# part 2
final_game_state, _ = play_game(format_data(data), recursion=True)
print(calculate_winner_score(final_game_state)) # 33259