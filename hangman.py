# This is the main module for the Hangman game.
# We can build it step by step, starting with the basic structure and then adding features incrementally later

# first let's write our features in our separate modules
# and then we can import them into our main module



# Overall structure of the game

### IMPORTS

from file_handling import load_word_list, save_to_leaderboard, view_leaderboard
from userdata_handling import UserData
from ui_handling import welcome_user, menu_user_options, graceful_exit
from gamelogic_handling import hangman_game, HangmanGame
import random
import time


### MAIN GAME LOOP
welcome_user() #welcome user to hangman / gamelogic handling
menu_user_options() # display menu options / UI handling file
user_choice = input("Please select an option (1-3): ")
if user_choice == "1":
    hangman_game() # start the game / gamelogic handling file
elif user_choice == "2":
    view_leaderboard() # view the leaderboard / file_handling file
elif user_choice == "3":
    graceful_exit() # exit the game / UI handling file
else:
    print("Invalid choice. Please try again.")



### PLAYING THE GAME - try not to use Class methods 
def hangman_game():
    username = input("Enter your name: ")
    user = UserData(username)

    word = random.choice(load_word_list())
    user.word = word
    game = HangmanGame(word)

    print(f"\n🕹️ Your word has {len(word)} letters.")
    print(game.generate_word_display())

    while not game.is_game_over():
        guess = input("🔤 Guess a letter: ")
        user.guesses.append(guess)
        print(game.guess_letter(guess))
        print("Word:", game.generate_word_display())
        print("Attempts remaining:", game.remaining_attempts())
        print()

    result = game.get_result()
    user.end_session(result)

    print("\n🎉 Game Over!")
    print(f"The word was: {word}")
    if result == "Win":
        print("🥳 You won!")
    else:
        print("💀 You lost. Try again!")

    save_to_leaderboard(user)
    

### Start the app
if __name__ == "__main__":
    # Entry point for the script
    welcome_user()
