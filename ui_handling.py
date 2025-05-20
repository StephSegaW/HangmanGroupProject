#Oksana
from gamelogic_handling import hangman_game


def menu_user_options() -> str:
    print("1. Start Game")
    print("2. View Leaderboard")
    print("3. Exit")
    user_input = input("Please select an option: ")
    if user_input == "1":
        hangman_game() #in gamelogic_handling
    elif user_input == "2":
        view_leaderboard() #in userdata_handling
    else:
        return "Exit" # this should be replaced with user choice
    
menu_user_options()

def graceful_exit():
    print("Thank you for playing Hangman!")
    print("Goodbye!")
    exit() # this will exit the program

# think about adding something for error handling