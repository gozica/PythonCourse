# IF and ELSE Statements
# if = Execute some code IF a condition is True
# elif = Test another condition if the previous ones are False
# else = Execute this code if none of the conditions are True

# ---------------------
#   EXAMPLE 1
# ---------------------

# Ask the user for their age
age = int(input("Enter your age: "))

# Check if the age is 100 or more
if age >= 100:
   print("You are too old to sign up")  # Message for age 100 or older

# Check if the age is 18 or more but less than 100
elif age >= 18:
   print("You are now signed up")  # Message for ages 18 to 99

# Check if the age is less than 0
elif age < 0:
   print("You haven't been born yet")  # Message for invalid age input

# If the age is less than 18
else:
   print("You must be 18+ to sign up")  # Message for underage users


# ---------------------
#   EXAMPLE 2
# ---------------------

# Ask the user if they want food
response = input("Do you want food (Y/N)?: ")

# Check if the response is "Y"
if response == "Y":
   print("Have some food")  # Provide food if the user says "Y"

# If the response is not "Y"
else:
   print("No food for you!")  # No food if the user says something else


# ---------------------
#   EXAMPLE 3
# ---------------------

# Ask the user for their name
name = input("Enter your name: ")

# Check if the user left the name empty
if name == "":
   print("You did not enter your name!")  # Message for missing name

# If the user entered a name
else:
   print(f"Hello {name}")  # Greet the user with their name


# ---------------------
#   EXAMPLE 4
# ---------------------

# Check if the user is online or offline
online = False  # Set the initial status to offline

# Check if the `online` variable is True
if online:
   print("You are online")  # Message if the user is online

# If the `online` variable is False
else:
   print("You are offline")  # Message if the user is offline
