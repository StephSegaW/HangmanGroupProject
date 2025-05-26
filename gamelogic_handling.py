import time
from draw import draw_hangman

def play_hangman(username, word):
    username = username.strip()
    guessed_letters = []
    correct_letters = set() # Use a set for correct letters to avoid duplicates
    tries = 8
    start_time = time.time()
    

    print(f"\n🕹️ The word has {len(word)} letters.")
    print("_ " * len(word))

    while tries > 0 and not all(letter in correct_letters for letter in word): # You have 8 guesses
        guess = input("Guess a letter: ").upper()
        if not guess.isalpha() or len(guess) != 1: #error handling
            print("Invalid input. Enter a single letter.")
            continue
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            correct_letters.add(guess) # Add the letter to correct letters set
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            tries -= 1
            print(f"❌ Nope. '{guess}' is not in the word.")
            draw_hangman(8 - tries)
        
        
        display = "".join([letter if letter in correct_letters else "_" for letter in word])
        print("\n Word:", display)
        print("\nTries left:", tries)
        print("\n")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

    # calculate the time taken
    display = "".join([letter if letter in correct_letters else "_" for letter in word])
    print("\nWord:", display)
    print("Tries left:", tries)
    print(f"Guessed letters: {', '.join(guessed_letters)}\n")

    # Check condition outside the loop
    # end of the game
    duration = round(time.time() - start_time, 2)

    if display == word and all(letter in correct_letters for letter in word): # Correct guess
        print(f"🎉 You guessed the word! It was '{word}'")
        print(f"⏱️ Time taken: {duration:.2f} seconds")
        return "Win", duration
        
    else:
        print(f"💀 You lost! The word was '{word}'")
        print(f"⏱️ Time taken: {duration:.2f} seconds")
        return "Loss", duration



    