# Keyword arguments let you name the arguments when calling a function, so you don’t have to remember the order.



#Think of introduce like a machine that takes inputs and gives an output!
def introduce(name, age, city):
    print(f"My name is {name}, I am {age} years old, and I live in {city}.")

# Using keyword arguments (order doesn't matter!)
introduce(name="nellz", age=25, city="Detroit")
introduce(city="New York", age=30, name="Alex")

# Makes the code easier to read
#You don’t have to remember the order of arguments
#Helps avoid mistakes when passing values

#exersice
# Function to greet the user based on their language preference
def greet_user(name, language="English"):
    if language == "Spanish":
        print(f"¡Hola, {name}!")
    elif language == "French":
        print(f"Bonjour, {name}!")
    elif language == "English":
        print(f"Hello, {name}!")
    else:
        print(f"Hello, {name}! (We don't speak {language} yet, but we'll try!)")

