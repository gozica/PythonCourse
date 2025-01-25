import random  # Importing the random module to generate random numbers

# Setting up the range of numbers for the guessing game
lowest_num = 1
highest_num = 100

# Generating a random number within the specified range
answer = random.randint(lowest_num, highest_num)

# To keep track of the number of guesses the player makes
gueses = 0

# A flag to keep the game running until the correct answer is guessed
is_running = True

# Welcome message and instructions
print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

# The main game loop
while is_running:

    # Prompt the user for a guess
    guess = input("Enter your guess:")

    # Check if the input is a number
    if guess.isdigit():
        guess = int(guess)  # Convert the input from a string to an integer
        gueses += 1  # Increment the guess counter

        # Check if the guess is out of the specified range
        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Select a number between {lowest_num} and {highest_num}")

        # If the guess is lower than the answer, tell the player to guess higher
        elif guess < answer:
            print("Too low! Try again")

        # If the guess is higher than the answer, tell the player to guess lower
        elif guess > answer:
            print("Too high! Try again")

        # If the guess is correct, end the game and show the number of guesses
        else:
            print(f"CORRECT! The answer is {answer}")
            print(f"Number of guesses: {gueses}")
            is_running = False  # Set the flag to False to exit the loop

    # If the input is not a number, prompt the user to enter a valid number
    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")
