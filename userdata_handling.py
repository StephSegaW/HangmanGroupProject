#Magda

#class UserData:                                     # The main class that holds all the data related to a single player session.
#    def __init__(self, username):
#       self.username = username                    # the name of the player
#       self.start_time = time.time()               # marks the game start time
#       self.guesses = []                           # an empty list for letters guessed by the player
#       self.word = ""                              # this will store the randomly selected word
#       self.result = ""                            # the outcome of the game – set to "win" or "lose" after the game ends

#Discuss if we need to switch to a dictionary
#add function to save the data


import random
from datetime import datetime

def select_random_word(word_list):
    return random.choice(word_list)

def update_guessed_word(secret_word, current_state, guessed_letter):
    return "", join([
        guessed_letter if secret_word[i] == guessed_letter else current_state[i]
        for i in range(len(secret_word))
    ])

def check_game_result(secret_word, current_state, attempts_left):
    if current_state == secret_word:
        return "win"
    elif attempts_left <= 0:
        return "lost"
    else:
        return "ongoing"
    
