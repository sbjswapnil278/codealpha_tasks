# Hangman Game

## Overview
This is a simple command-line Hangman game implemented in Python. The player tries to guess a randomly selected word by guessing one letter at a time. The game allows a limited number of incorrect guesses before ending.

## Features
- Randomly selects a word from a predefined list.
- Displays the word progress with underscores for unguessed letters.
- Tracks guessed letters to avoid repeated guesses.
- Limits the number of incorrect guesses to 6.
- Validates user input (only single alphabetic characters allowed).
- Provides feedback on guesses.
- Congratulates the player upon success or reveals the correct word upon failure.

## How to Play
1. Run the Python script.
2. The game will show the number of incorrect guesses allowed and the word with hidden letters.
3. Enter one letter at a time to guess the word.
4. The game will indicate if the guess was correct or wrong.
5. Continue guessing until the word is fully revealed or the maximum incorrect guesses are reached.

## Requirements
- Python 3

## Running the Game
Run the script using the command:
python hangman.py
