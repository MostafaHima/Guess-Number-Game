import random
import os
import pyfiglet

# Display ASCII art for the game title
ascii_art = pyfiglet.figlet_format("Guess Number")
print(ascii_art)

# Function to clear the terminal screen
def clear_screen():
    if os.name == 'nt':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux/Mac

# Welcome message
clear_screen()
print(
    f"""
    Welcome to the Guess a Number Game!
    I'm thinking of a number between 1 and 100
    ----------------------------------------------
    """
)

# Main game function
def play_game():
    """
    Function to run the main guessing game.
    """
    # Function to handle user guesses
    def guess_number(random_number, difficulty):
        attempts_left = 0
        game_active = True

        # Set the number of attempts based on difficulty
        if difficulty == "easy":
            attempts_left = 10
        elif difficulty == "hard":
            attempts_left = 5
        else:
            print("Invalid choice. Restarting the game...")
            return play_game()

        print(f"\nYou have {attempts_left} attempts remaining to guess the number.\n")

        # Game loop for user guesses
        while attempts_left > 0 and game_active:
            try:
                user_guess = int(input("Make a guess: "))
            except ValueError:
                print("\nInvalid input. Please enter a number.\n")
                continue

            # Compare the user's guess to the random number
            if user_guess > random_number:
                print("\nToo high. Try again.\n")
            elif user_guess < random_number:
                print("\nToo low. Try again.\n")
            else:
                game_active = False
                return "Congratulations! You guessed the number correctly."

            # Deduct attempts if the guess is incorrect
            attempts_left -= 1
            print(f"You have {attempts_left} attempts remaining.\n")

        # If the user runs out of attempts
        return f"Sorry, you've run out of attempts. The correct number was {random_number}."

    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)

    # Prompt the user to select difficulty
    user_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
    print(guess_number(random_number, user_difficulty))

# Loop to allow replaying the game
while input("Do you want to play? Type 'Y' for Yes or 'N' for No: ").strip().lower() == "y":
    clear_screen()
    play_game()

# End message after exiting the game
clear_screen()
print("Thank you for playing the Guess a Number Game! Come back soon.")
