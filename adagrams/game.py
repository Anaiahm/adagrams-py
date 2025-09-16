from random import randint
import random

LETTER_POOL = {
    1: 'A', 2: 'A', 3: 'A', 4: 'A', 5: 'A', 6: 'A', 7: 'A', 8: 'A', 9: 'A',
    10: 'B', 11: 'B',
    12: 'C', 13: 'C',
    14: 'D', 15: 'D', 16: 'D', 17: 'D',
    18: 'E', 19: 'E', 20: 'E', 21: 'E', 22: 'E', 23: 'E', 24: 'E', 25: 'E', 26: 'E', 27: 'E', 28: 'E', 29: 'E',
    30: 'F', 31: 'F',
    32: 'G', 33: 'G', 34: 'G',
    35: 'H', 36: 'H',
    37: 'I', 38: 'I', 39: 'I', 40: 'I', 41: 'I', 42: 'I', 43: 'I', 44: 'I', 45: 'I',
    46: 'J',
    47: 'K',
    48: 'L', 49: 'L', 50: 'L', 51: 'L',
    52: 'M', 53: 'M',
    54: 'N', 55: 'N', 56: 'N', 57: 'N', 58: 'N', 59: 'N',
    60: 'O', 61: 'O', 62: 'O', 63: 'O', 64: 'O', 65: 'O', 66: 'O', 67: 'O',
    68: 'P', 69: 'P',
    70: 'Q',
    71: 'R', 72: 'R', 73: 'R', 74: 'R', 75: 'R', 76: 'R',
    77: 'S', 78: 'S', 79: 'S', 80: 'S',
    81: 'T', 82: 'T', 83: 'T', 84: 'T', 85: 'T', 86: 'T',
    87: 'U', 88: 'U', 89: 'U', 90: 'U',
    91: 'V', 92: 'V',
    93: 'W', 94: 'W',
    95: 'X',
    96: 'Y', 97: 'Y',
    98: 'Z',
}

MAX_HAND_SIZE = 10
MIN_LETTER_OCCURANCE = 1
MAX_LETTER_OCCURANCE = 100

SCORE_CHART = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1,
    'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}

def draw_letters():
    hand = []
    while len(hand) < MAX_HAND_SIZE:
        hand.append(get_new_letter())
    return hand

def get_new_letter():
    new_letter_value = random.randint(MIN_LETTER_OCCURANCE, MAX_LETTER_OCCURANCE)
    new_letter = LETTER_POOL[new_letter_value]
    return new_letter

def uses_available_letters(word, letter_bank):
    word = capitalize_word(word)
    for letter in word:
        if letter not in letter_bank:
            return False
        else:
            word_letter_frequency = check_letter_frequency(word)
            hand_letter_frequency = check_letter_frequency(letter_bank)
            if word_letter_frequency[letter] > hand_letter_frequency[letter]:
                return False
            else:
                all_lettes_are_in_hand = True
    return all_lettes_are_in_hand
        
def capitalize_word(word):
     word = word.upper()
     return word

def check_letter_frequency(x):
    letter_count = {}
    for letter in x:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    return letter_count

def score_word(word):
        word = capitalize_word(word)
        total_score = calculate_total_score(word)
        if len(word) > 6:
            total_score += 8
        return total_score
    
def calculate_total_score(word):
    total_score = 0
    for letter in word:
        letter_point = SCORE_CHART[letter]
        total_score += letter_point
    return total_score
    

def get_highest_word_score(word_list):
    scores_list = [] 
    for word in word_list:
        total_score = score_word(word)
        scores_list.append(total_score)
    # print(scores_list)
    # print(word_list)
    score_pointer = 0
    for score in scores_list:
        current_score = score
        if current_score > score_pointer:
            score_pointer = current_score
        else:
            continue
    # print(score_pointer)
        
    # a_variable_that_shall_not_be_named = ()
    winning_word_data = (word_list[scores_list.index(score_pointer)],score_pointer)
    # print(a_variable_that_shall_not_be_named)
    return winning_word_data
     












# -----------------------Pseudocode_______________________
    #   Wave 1
# if the player has less than 10 tiles (the maximun allowed) in their hand 
    # new_letter = get_new_letter() ***
    # draw another tile ****
    # draw another tile  and add the drawn tile to their hand 

# the function to draw a new tile

        # Wave 2 

    # uses_available_letters
    # for each letter in word:
    #     if letter not in list:
    #         return False 
    # letter_bank = [R, I, I, T, T, Y, W, E, C, F] word = WITTY
# def check_letter_frequency(letter_bank):
#     letter_count = {}
#     for letter in letter_bank:
#         if letter not in letter_count:
#             letter_count[letter] = 1
#         else:
#             letter_count[letter] += 1
#     return letter_count


    #    wave 3
    # def score_word(word):
    


        #   wave 4

    # def get_highest_word_score(word_list):
    #     scores_list = [] 
    #     for word in word_list:
    #         total_score = score_word(word)
    #         scores_list.append(total_score)
    #     winning_word_data = a tuple
    #     tuple[0] = word_list[highest score]
    #     tuple[1] = highest score in scores_liss
    #     return winning_word_data


    #     a_variable_that_shall_not_be_named = {}
    #     a_variable_that_shall_not_be_named[0] = word_list[0]
        
        

# 