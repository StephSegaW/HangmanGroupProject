

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



#Quiz Game Example


import json
import operator
import random
from datetime import datetime 

def save_score(username, score, total_questions):
    # Create a dictionary to store the current score entry
    score_entry = {
        'username': username,
        'score': score,
        'total_questions': total_questions,
        'percentage': (score/total_questions)*100,
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Load existing scores from the JSON file
    # remember to import json file to handle the leaderboard
    try:
        with open('python_quiz_leaderboard.json', 'r') as file:
            leaderboard = json.load(file)

    # If there aren't any scores yet, catch the error and continue with an empty list
    except FileNotFoundError:
        leaderboard = []

    # Add the current score entry to the leaderboard
    leaderboard.append(score_entry)

    # Sort the leaderboard by score in descending order
    leaderboard.sort(key=operator.itemgetter('score'), reverse=True)

    # Keep only the top 10 scores
    leaderboard = leaderboard[:10]

    # Save the updated leaderboard
    with open('python_quiz_leaderboard.json', 'w') as file:
        json.dump(leaderboard, file, indent=4)


# remember to import json file to handle the leaderboard
def view_leaderboard():
    # Load the leaderboard from the JSON file
    try:
        with open('python_quiz_leaderboard.json', 'r') as file:
            leaderboard = json.load(file)
            print("\n\n--- Leaderboard ---")
            for entry in leaderboard:
                print(f"{entry['username']}: {entry['score']}/{entry['total_questions']} ({entry['percentage']:.2f}%) on {entry['date']}")
    except FileNotFoundError:
        print("No leaderboard data found.")