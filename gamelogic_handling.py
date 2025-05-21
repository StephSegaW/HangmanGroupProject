#Ramia
from file_handling import get_word

def welcome_user():
    print("Welcome to Hangman!")
    return 


# ---- DRAW FUNCTION (stub) ----
def draw_hangman(stage):
    print(f"[HANGMAN STAGE {stage}]")  # Replace with actual drawing if needed

# ---- USERDATA HANDLING (stub) ----
def save_score(username, result):
    print(f"(Score saved for {username}: {result})")

def show_leaderboard():
    print("(Leaderboard feature coming soon!)")

# ---- GAME CLASS ----
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
            return f"✅ Good job! '{letter}' is in the word."
        else:
            self.incorrect_guesses.add(letter)
            draw_hangman(len(self.incorrect_guesses))
            return f"❌ Sorry, '{letter}' is not in the word."

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

# ---- GAME RUNNER FUNCTION ----
def load_word_list(filename="word_list.txt"): #get word list from file
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("⚠️ word_list.txt not found. Using default word list.")
        return ["laptop", "pencil", "book"]

def get_word():
    word_list = load_word_list()
    return random.choice(word_list)


def hangman_game():
    print("🎮 Welcome to Hangman!")
    username = input("Enter your name: ")

    while True:
        word = get_word()
        game = HangmanGame(word)

        print("\nThe word has", len(word), "letters.")
        print(game.generate_word_display())

        while not game.is_game_over():
            guess = input("Guess a letter: ")
            print(game.guess_letter(guess))
            print("Word:", game.generate_word_display())
            print("Incorrect guesses:", game.get_incorrect_guesses())
            print("Attempts remaining:", game.remaining_attempts())
            print()

        print("\n✅ Game Over!")
        print("The word was:", game.word)
        result = game.get_result()

        if result == "Win":
            print("🎉 You guessed the word!")
        else:
            print("💀 You ran out of attempts. Better luck next time.")

        save_score(username, result)

        choice = input("\nPlay again (P), Show leaderboard (L), or Quit (Q)? ").upper()
        if choice == "L":
            show_leaderboard()
        elif choice == "Q":
            print("👋 Goodbye!")
            break

# ---- RUN THE GAME ----
if __name__ == "__main__": #
    hangman_game() 



#---------------------------------------------------------------------------------------------



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



