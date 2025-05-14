# This is the main module for the Hangman game.
# We can build it step by step, starting with the basic structure and then adding features incrementally later

# first let's write our features in our separate modules
# and then we can import them into our main module



# Overall structure of the game

# 1. Import necessary modules 
### Random for random word selection
import random 
from file_handling import get_word
from ui_handling import menu_user_options
from gamelogic_handling import welcome_user


### Hangman Drawing
### Winning and losing conditions

# 2. Detailed game logic
### Word selection
### Initial game setup

### Main game loop

welcome_user() #welcome user to hangman
user_choice = menu_user_options() # display menu options, show the user options
# Oksana will finish the if statement for the menu options
graceful_exit()



###     User input
###     Check the Guess
###     Display the game state
###     End of turn
###     Game End

# 3. Error handling
### Invalid input - Check for non-alphabetic characters/multiple letters
### Repeated guesses - Check if the letter has already been guessed
### File not found - word file missing, user data file issue
### Out of guesses
### Graceful exit

