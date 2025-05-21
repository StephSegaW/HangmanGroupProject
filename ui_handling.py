#Oksana
from gamelogic_handling import hangman_game

def welcome_user():
    print("Welcome to Hangman!")
    print("-" * 30)


def menu_user_options() -> str:
    print("Main Menu:")
    print("1. Start Game")
    print("2. View Leaderboard")
    print("3. Exit")


def graceful_exit():
    print("Thank you for playing Hangman!")
    print("Goodbye!")
    exit() # this will exit the program
