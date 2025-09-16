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
    98: 'Z'
}

MAX_HAND_SIZE = 10
MIN_LETTER_OCCURANCE = 1
MAX_LETTER_OCCURANCE = 98

def draw_letters():
    hand = []
    while len(hand) < MAX_HAND_SIZE:
        hand.append(get_new_letter())
    return hand

def get_new_letter():
    new_letter_value = random.randint(MIN_LETTER_OCCURANCE, MAX_LETTER_OCCURANCE)
    new_letter = LETTER_POOL[new_letter_value]
    # print(new_letter)
    return new_letter

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass


# -----------------------Pseudocode_______________________

# if the player has less than 10 tiles (the maximun allowed) in their hand 
    # new_letter = get_new_letter() ***
    # draw another tile ****
    # draw another tile  and add the drawn tile to their hand 

# the function to draw a new tile
