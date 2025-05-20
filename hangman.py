# This is the main module for the Hangman game.
# We can build it step by step, starting with the basic structure and then adding features incrementally later

# first let's write our features in our separate modules
# and then we can import them into our main module



# Overall structure of the game

# 1. Import necessary modules 
### Random for random word selection
import random 
from file_handling import get_word
from ui_handling import menu_user_options, graceful_exit
from gamelogic_handling import welcome_user, hangman_game


### Hangman Drawing
### Winning and losing conditions

# 2. Detailed game logic
### Word selection
### Initial game setup

### MAIN GAME LOOP
welcome_user() #welcome user to hangman / gamelogic handling
user_choice = menu_user_options() # display menu options / UI handling file
if user_choice == "Start Game":
    hangman_game() # start the game / gamelogic handling file
if user_choice == "View Leaderboard":
    view_leaderboard() # view the leaderboard / userdata handling file
if user_choice == "Exit":
    graceful_exit() # exit the game / UI handling file




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

