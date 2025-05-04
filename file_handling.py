

import os

def read_file(file_path: str) -> str:
    """
    Reads the content of a file and returns it as a string.
    
    :param file_path: Path to the file to be read.
    :return: Content of the file as a string.
    """
    # code implemented here
    raise NotImplementedError("File reading not implemented yet.")




# FILE HANDLING FEATURES
# These features handle file operations for the Hangman game.
# It includes functions to load words from the word list file and save the score into userdata.
# Loading the word list from a file
import random # This module is used to generate random words for the game.
from words import word_list

# Selects a random word from the word list
def get_word(): 
    word = random.choice(word_list)
    return word.upper() # Converts the word to uppercase for consistency


# Saving the score into userdata
def save_score(score, filename='userdata.txt'): # Needs userdata.txt to be created - Magda
    with open(filename, 'a') as file: # Opens the file in append mode
        file.write(f"{score}\n") # Appends the score to the userdata file
