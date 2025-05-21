
# FILE HANDLING FEATURES
# These features handle file operations for the Hangman game.
# It includes functions to load words from the word list file, save the score into userdata and show the leaderboard.


def load_word_list(filename = "word_list.txt"):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return []
    
def save_to_leaderboard(username, filename = "leaderboard.txt"):
    with open(filename, 'a') as file:
        file.write(f"{user.username}, {user.result}, {user.duration}s\\n")

def view_leaderboard(filename = "leaderboard.txt"):
   print("Leaderboard:")
   try:
       with open(filename, 'r') as file:
           for line in file:
               name, result, duration = line.strip().split(", ")
               print(f"{name} - {result} in {duration}")
   except FileNotFoundError:
       print(f"Error: The file {filename} was not found.")
       


#-------------------------------------------------------------------------------------


import os

def read_file(file_path: str) -> str:
    """
    Reads the content of a file and returns it as a string.
    
    :param file_path: Path to the file to be read.
    :return: Content of the file as a string.
    """
    # code implemented here
    raise NotImplementedError("File reading not implemented yet.")



