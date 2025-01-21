# 2D List: A list of lists (like a table or grid where each row is a separate list)

# A list of fruits
fruits = ["apple", "orange", "banana", "coconut"]

# A list of vegetables
veggies = ["celery", "pepper", "carrot"]

# A list of meats
meats = ["chicken", "beef", "turkey"]

# Combine the above lists into one big list (each list becomes a "row" in the 2D list)
groceries = [fruits, veggies, meats]

# Print a specific item from the 2D list
print(groceries[1][1])
# Explanation:
# - groceries[1] means "get the second list" (index 1 is veggies because counting starts at 0)
# - groceries[1][1] means "from the second list, get the second item" (index 1 is "pepper")

# Output: pepper

# This is a pretend number pad, like the one on a phone.
# It’s a list of rows. Each row has numbers or symbols in it.
num_pad = [[1, 2, 3],        # First row of the number pad
           [4, 5, 6],        # Second row
           [7, 8, 9],        # Third row
           ["*", 0, "#"]]    # Fourth row with special symbols

# We want to print out all the rows, one by one, like a real number pad!

# Outer loop: Go through each row in the number pad.
for row in num_pad:
    # Inner loop: Look at each number or symbol in the row.
    for num in row:
        print(num, end=" ")  # Print the number or symbol, but stay on the same line.
    print()  # After finishing one row, move to a new line.
