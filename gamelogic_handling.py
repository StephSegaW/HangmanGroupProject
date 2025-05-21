#Ramia
#This file contains the logic for the hangman game
# It includes the game loop, user input handling, and game state management

# Ensure draw.py exists in the same directory or update the import path accordingly
try:
    from draw import draw_hangman
except ImportError:
    def draw_hangman(attempts):
        print(f"[Placeholder] Draw hangman with {attempts} incorrect attempts.")

class HangmanGame:
    def __init__(self, word, max_attempts=8):
        self.word = word.lower()
        self.max_attempts = max_attempts
        self.correct_guesses = set()
        self.incorrect_guesses = set()

    def guess_letter(self, letter):
        letter = letter.lower()
        if not letter.isalpha() or len(letter) != 1:
            return "Invalid input. Please enter a single letter."
        if letter in self.correct_guesses or letter in self.incorrect_guesses:
            return f"You already guessed '{letter}'."
        if letter in self.word:
            self.correct_guesses.add(letter)
            return f"Good job! '{letter}' is in the word."
        else:
            self.incorrect_guesses.add(letter)
            draw_hangman(len(self.incorrect_guesses))
            return f"Sorry, '{letter}' is not in the word."

    def generate_word_display(self):
        return " ".join([letter if letter in self.correct_guesses else "_" for letter in self.word])

    def is_word_guessed(self):
        return all(letter in self.correct_guesses for letter in self.word)

    def remaining_attempts(self):
        return self.max_attempts - len(self.incorrect_guesses)

    def is_game_over(self):
        return self.is_word_guessed() or self.remaining_attempts() <= 0

    def get_incorrect_guesses(self):
        return sorted(self.incorrect_guesses)

    def get_result(self):
        if self.is_word_guessed():
            return "Win"
        elif self.remaining_attempts() <= 0:
            return "Loss"
        return "In Progress"

#---------------------------------------------------------------------------------------------




