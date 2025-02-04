# Default arguments = Automatic values for some parameters
# If no value is given, the program uses these defaults


#simple example
def greet(name="Friend"):  # Default name is "Friend" if no name is given
    print(f"Hello, {name}!")

greet()          # Uses the default name "Friend"
greet("nellz")   # Uses the name "nellz"


# ---- EXERCISE ----

import time  # Imports time module to use the sleep function

# Function to count numbers from start to end
def count(end, start=0):  # Default start is 0 if not provided
    for x in range(start, end + 1):  # Loops from start to end
        print(x)  # Prints each number
        time.sleep(1)  # Waits 1 second before printing the next number
    print("DONE!")  # Prints "DONE!" when counting is finished

count(10)       # Counts from 0 to 10 (default start = 0)
count(30, 15)   # Counts from 15 to 30
