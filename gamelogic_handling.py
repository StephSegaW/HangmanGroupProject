#Ramia
from file_handling import get_word

def welcome_user():
    print("Welcome to Hangman!")
    return 

def hangman_game():
    #get random word from list of words
    get_word()
    #print the number of letters in the word
    #let the user guess the letter or word
    #check if the letter is in the word
    #if the letter is in the word, print the letter in the correct position
    #if the letter is not in the word, print the letter and decrement the number of guesses
    #limit of guesses is 8 (forloop)
    #save the user and score in userdata_handling file