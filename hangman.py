# This is the main module for the Hangman game.
# We can build it step by step, starting with the basic structure and then adding features incrementally later

# first let's write our features in our separate modules
# and then we can import them into our main module
# import time and drawing functions are in gamelogic_handling.py
# import random and os are in file_handling.py
# ui and userdata is handled in hangman.py



# ISSUE - you are welcome to fix
## in def main_menu, it does not loop back after input error. Example: user input - sdfjsalk, app closes and not return to main menu option




# Importing necessary modules into hangman.py
from file_handling import view_leaderboard, load_words_from_file, save_to_leaderboard
from gamelogic_handling import play_hangman


# A function is created to display Main Menu and handle user input
# The main menu presents 3 options for the user: play hangman game / show leaderboard / end app
def main_menu():
    print("\n======= HANGMAN MAIN MENU =======")
    print("1. Play Hangman")
    print("2. View Leaderboard")
    print("3. Exit")
    choice = input("Choose an option (1-3): ")
    if choice == "1": # Play Hangman
        username = input("Enter your name: ")
        word = load_words_from_file().upper() # random is imported in file_handling.py
        result, duration = play_hangman(username, word) # username and word are passed to play_hangman function
        save_to_leaderboard(username, result, duration) # The result and duration are passed to save_to_leaderboard function
        return ask_play_again()
    elif choice == "2": # View Leaderboard
        view_leaderboard()
        return ask_return_to_menu()
    elif choice == "3": # Exit
        print("👋 Thanks for playing! Goodbye.")
        return
    else:
        print("Invalid input. Please try again.")

# A function is created from choice 1's return calls the function to play the game again
def ask_play_again():
    print( "\n======= GOODGAME =======")
    print("1. Return to Main Menu")
    print("2. Play Again")
    print("3. Exit")
    choice = input("Return to Main Menu or Exit (1-3): ")
    if choice == "1":
        return main_menu()  # Restart the game
    elif choice == "2":
        username = input("Enter your name: ")
        word = load_words_from_file().upper() # random is imported in file_handling.py
        result, duration = play_hangman(username, word) # username and word are passed to play_hangman function
        save_to_leaderboard(username, result, duration) # The result and duration are passed to save_to_leaderboard function
        return ask_play_again()  # Play again with the same username and word
    elif choice == "3":
        print("👋 Thanks for playing! Goodbye.")
        return
    else:
        print("Invalid input. Please try again.")
        return ask_play_again()
    
# A function is created from choice 2's return calls the function to return to the main menu
def ask_return_to_menu():
    print("\n===================")
    print("1. Return to Main Menu")
    print("2. Exit")
    choice = input("Return to Main Menu or Exit (1-2): ")
    if choice == "1":
        return main_menu()  # Restart the game
    elif choice == "2":
        print("👋 Thanks for playing! Goodbye.")
        return
    else:
        print("Invalid input. Please try again.")
        return ask_return_to_menu()
    
# Main function to start the app
if __name__ == "__main__":
    main_menu()
