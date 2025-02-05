# Membership operators = used to test whether a value or variable is found in a sequence
#                                             (string, list, tuple, set, or dictionary)
#                                             1. in = boolean
#                                             2. not in = does the opposite of in

# --------------------
# EXAMPLE 1
# --------------------
word = "APPLE"  # Defining a string with the word "APPLE"

# Asking the user to guess a letter
letter = input("Guess a letter in the secret word: ")

# Checking if the guessed letter is in the word
if letter in word:
    print(f"There is a {letter}")  # If the letter is found, print a message
else:
    print(f"{letter} was not found")  # If the letter is not found, print a message

# --------------------
# EXAMPLE 2
# --------------------
students = {"Spongebob", "Patrick", "Sandy"}  # A set of student names

# Asking the user for a student's name
student = input("Enter the name of a student: ")

# Checking if the student is in the set of students
if student in students:
    print(f"{student} is in this class")  # If the student is found, print a message
else:
    print(f"{student} is NOT in this class")  # If the student is not found, print a message

# --------------------
# EXAMPLE 3
# --------------------
grades = {
    "Sandy": 'A',
    "Squidward": 'B',
    "Spongebob": 'C',
    "Patrick": 'D'
}  # A dictionary of student names and their grades

# Asking the user for a student's name to check their grade
student = input("Enter the name of a student: ")

# Checking if the student is in the grades dictionary
if student in grades:
    print(f"{student}'s grade is {grades[student]}.")  # If the student is found, print their grade
else:
    print(f"{student} is not in the dictionary")  # If the student is not found, print a message

# --------------------
# EXAMPLE 4
# --------------------
email = "BroCode@gmail.com"  # A sample email string

# Checking if both "@" and "." are present in the email string
if "@" in email and "." in email:
    print("Valid email")  # If both symbols are found, print a message
else:
    print("Invalid email")  # If either symbol is missing, print a message


