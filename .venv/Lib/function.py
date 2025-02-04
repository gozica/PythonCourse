#function = A block of reusable code
#           place () after the function to invoke it



#A function is like a recipe for your code. It lets you write instructions once and use them over
# and over again. This makes your code shorter, cleaner, and easier to manage.

# A function is like a recipe: you write it once and use it multiple times

# Example 1: Function to display a bill reminder
def display_invoice(username, amount, due_date):
    # This function prints a bill reminder for a user
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")


# Calling the function with different values
display_invoice("Nellz", 42.50, "01/02")
display_invoice("JoeSchmo", 100.99, "02/03")


# Example 2: Function to format a name
def create_name(first, last):
    # Capitalize the first letter of both the first and last names
    first = first.capitalize()
    last = last.capitalize()

    # Combine the names and return the full name
    return first + " " + last


# Calling the function and storing the result in full_name
full_name = create_name("spongebob", "squarepants")
print(full_name)  # Output: Spongebob Squarepants
