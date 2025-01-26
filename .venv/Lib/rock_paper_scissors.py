import random  # Importing the random module to let the computer make random choices

# A tuple containing the three options for the game
options = ("rock", "paper", "scissors")

# A flag to keep the game running until the player decides to quit
running = True

# Main game loop
while running:
    player = None  # This will hold the player's choice
    computer = random.choice(options)  # The computer randomly selects an option

    # Keep asking the player for a valid choice until they enter one of the options
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()  # Convert input to lowercase

    # Show the player's and computer's choices
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    # Check for a tie
    if player == computer:
        print("It's a tie!")

    # Check if the player wins
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")

    # If none of the winning conditions match, the player loses
    else:
        print("You lose!")

    # Ask the player if they want to play again or quit
    player = input("PLAY AGAIN? Press Enter to continue or type (q to quit): ").lower()

    # If the player enters 'q', stop the game
    if player == "q":
        running = False

