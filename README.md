# Guess Number Game

## Introduction
The **Guess Number Game** is a simple interactive Python program where the user tries to guess a randomly generated number. The program provides difficulty levels and gives feedback to guide the player.

## Features
- **Dynamic Difficulty**: Choose between 'easy' (10 attempts) or 'hard' (5 attempts).
- **Clear Feedback**: The program informs you if your guess is too high or too low.
- **Replayable**: Play as many times as you'd like without restarting the program.

## How to Run
1. Ensure you have **Python 3.x** installed on your system.
2. Clone or download the project files.
3. Run the script using the terminal:
   ```bash
   python main.py
   ```

## Rules
1. The computer generates a random number between 1 and 100.
2. Select a difficulty level:
   - **Easy**: 10 attempts to guess the number.
   - **Hard**: 5 attempts to guess the number.
3. Enter a number when prompted.
4. Feedback will guide you whether your guess is:
   - **Too High**
   - **Too Low**
5. You win by guessing the correct number within the allowed attempts.

## Example Run
```
Welcome to the Guess a Number Game!
I'm thinking of a number between 1 and 100
----------------------------------------------

Choose a difficulty. Type 'easy' or 'hard': easy

You have 10 attempts remaining to guess the number.
Make a guess: 50
Too low. Try again.
You have 9 attempts remaining.

Make a guess: 75
Too high. Try again.
You have 8 attempts remaining.

Make a guess: 63
Congratulations! You guessed the number correctly.
```

## Requirements
- Python 3.x

## Dependencies
- `pyfiglet`: For displaying ASCII art (install it using `pip install pyfiglet`).


