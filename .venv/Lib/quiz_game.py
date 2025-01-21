# fun quiz game written in Python

# Create a list of questions to ask in the quiz.
questions = (
    "In what country did the first Starbucks open outside of North America? ",  # Question 1
    "In a website browser address bar, what does www stand for? ",  # Question 2
    "Originally, Amazon only sold what kind of product? ",  # Question 3
    "Who painted the Mona Lisa? ",  # Question 4
    "Who was the first woman pilot to fly solo across the Atlantic? "  # Question 5
)

# Create a list of possible answers (options) for each question.
options = (
    ('A. Japan', 'B. China', 'C. Germany', 'D. Africa'),  # Options for Question 1
    ('A. World Wide Web', 'B. World Web Will', 'C. Who What Web', 'D. Will Wake Web'),  # Question 2
    ('A. Clothes', 'B. Books', 'C. Groceries', 'D. CDs'),  # Question 3
    ('A. Kanye West', 'B. Van Gogh', 'C. Leonardo da Vinci', 'D. Bob Ross'),  # Question 4
    ('A. Beyonce', 'B. Marie Will', 'C. Madam C.J. Walker', 'D. Amelia Earhart')  # Question 5
)

# Store the correct answers for each question.
answers = ('A', 'A', 'B', 'C', 'D')

# Initialize an empty list to keep track of the player's guesses.
guesses = []

# Start the score at 0. The score will increase when the player gets a correct answer.
score = 0

# Create a variable to track which question we're on. It starts at 0 (the first question).
question_num = 0

# Loop through all the questions, one by one.
for question in questions:
    print("---------------------------")  # Print a separator to make the output look clean
    print(question)  # Print the current question

    # Loop through all the options for the current question
    for option in options[question_num]:
        print(option)  # Print each option

    # Ask the player for their answer to the current question
    guess = input('Enter (A, B, C, D): ').upper()  # Convert the input to uppercase for consistency
    guesses.append(guess)  # Add the player's guess to the list of guesses

    # Check if the player's guess matches the correct answer for the current question
    if guess == answers[question_num]:
        score += 1  # If correct, increase the score by 1
        print('CORRECT!')  # Tell the player they got it right
    else:
        print('INCORRECT!')  # Tell the player they got it wrong
        print(f'The correct answer is {answers[question_num]}.')  # Show the correct answer

    # Move to the next question by increasing the question number by 1
    question_num += 1

# After all the questions, show the player's final score
print("---------------------------")
print(f"You got {score}/{len(questions)} correct!")  # Show the score and the total number of questions
