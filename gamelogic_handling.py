#Ramia
from file_handling import get_word

def welcome_user():
    print("Welcome to Hangman!")
    return 

from draw import draw_hangman # This will draw the hangman when needed
class HangmanGame:
    def __init__(self, word, max_attempts=8): # Initialize the game with a word and max attempts
        self.word = word.lower()
        self.max_attempts = max_attempts
        self.correct_guesses = set()
        self.incorrect_guesses = set()
    def guess_letter(self, letter):
        letter = letter.lower()
        # check if input is valid
        if not letter.isalpha() or len(letter) != 1:
            return "Invalid input. Please enter a single letter."
        # check for repeated guesses
        if letter in self.correct_guesses or letter in self.incorrect_guesses:
            return f"You already guessed '{letter}'."
        # check if the letter is correct
        if letter in self.word:
            self.corrects_guesses.add(letter)
            return f"Good job! '{letter}' is in the word."
        else:
            self.incorrect_guesses.add(letter)
            draw_hangman(len(self.incorrect_guesses))
            return f"Sorry, '{letter}' is not in the word."
    def generate_word_display(self):
        # Show the word with guessed letters and _ for the rest
        return " ".join([letter if letter in self.correct_guesses else "_" for letter in self.word])
    def is_word_guessed(self):
        # Check if all letters in the word are guessed
        return all(letter in self.corrects_guesses for letter in self.word)
    def remaining_attempts(self):
        return self.max_attempts - len(self.incorrect_guesses)
    def is_game_over(self):
        # Game ends if the word is guessed () or no more attempts
        return self.is_word_guessed() or self.remaining_attempts() <= 0
    def get_incorrect_guesses(self):
        return sorted(self.correct_guesses)
    def get_result(self):
        if self.is_word_guessed():
            return "Win"
        elif self.remaining_attempts() <= 0:
            return "loss"
        return "in progress"



def hangman_game():
    #get random word from list of words
    #limit of guesses is 8 (forloop)
    get_word()
    #print the number of letters in the word _ _ _ _ _
    #let the user guess the letter or word
    #check if the letter is in the word
        #if the letter is in the word, print the letter in the correct position
        #if the letter is in the word, print the letter and increment the number of guesses
        #if the letter is not in the word, print the letter and decrement the number of guesses and draw 1 part of the hangman 
    #if user uses all the guesses, print the word and say they lost
    #if user guesses the word, print the word and say they won
    #if user wants to play again, restart the game
    #if user wants to quit, exit the game
    #if user wants to see the leaderboard, show the leaderboard
    #save the user and score in userdata_handling file



