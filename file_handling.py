import os
import random

def load_words_from_file(filename="word_list.txt"):
    try:
        with open(filename, "r") as f:
            words = [line.strip() for line in f if line.strip()]
        return random.choice(words)
    except FileNotFoundError:
        print("⚠️ word_list.txt not found. Using fallback words.")
        return random.choice(["default", "python", "hangman"])

def save_to_leaderboard(username, result, duration):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{username},{result},{duration:.2f}s\n")

def view_leaderboard():
    if not os.path.exists("leaderboard.txt"):
        print("🏆 No leaderboard data yet.")
        return
    print("\n🏆 Leaderboard:")
    with open("leaderboard.txt", "r") as file:
        for line in file:
            name, result, duration = line.strip().split(",")
            print(f"👤 {name} | Result: {result} | Time: {duration}")