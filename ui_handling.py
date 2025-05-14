#Oksana
from gamelogic_handling import hangman_game

def menu_user_options() -> str:
    print("1. Start Game")
    print("2. View Leaderboard")
    print("3. Exit")
    if user_input == "1":
        hangman_game()
    elif user_input == "2":
        view_leaderboard()
    else
    return "Exit" # this should be replaced with user choice

# think about adding something for error handling