# Number Guessing Game 🎲 (Computer Guesses You)

A simple Python game where **the computer tries to guess your number** between 1 and 100 using your feedback: "higher", "lower", or "correct".

## How It Works
- You think of a number between 1 and 100.
- The computer makes a guess.
- After each guess, you tell it:
  - `"higher"` if your number is greater than the guess
  - `"lower"` if your number is less than the guess
  - `"correct"` if it guessed right
- The game ends when the computer guesses correctly.

## How to Run

```bash
python number_guessing_game.py

Think of a number between 1 and 100...
My guess is 42
higher, lower, or correct? higher
My guess is 71
higher, lower, or correct? lower
My guess is 56
higher, lower, or correct? correct
I told you I was going to guess your number...

Requirements
Python 3.x