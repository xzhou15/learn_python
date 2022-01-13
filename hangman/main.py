#!/usr/bin/env python3
"""A hangman game written in Python."""

import random
import requests
from hangman_art import stages, logo
from hangman_words import word_list
from clear_console import clear

print(logo)
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
URL = "https://api.dictionaryapi.dev/api/v2/entries/en/" + chosen_word
resp = requests.get(URL).json()
definition = resp[0]["meanings"][0]["definitions"][0]["definition"]

display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lost a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            clear()
            print("You lost.")
            print(f"The word was {chosen_word}.")
            print(f"Definition: {definition}")
    
    if not "_" in display:
        game_is_finished = True
        print("You won!")

    print(stages[lives])
