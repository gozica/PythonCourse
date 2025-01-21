# Nested Loop Example: A program to create a grid of symbols

# Ask the user for the number of rows in the grid
rows = int(input("Enter the number of rows: "))

# Ask the user for the number of columns in the grid
col = int(input("Enter the number of columns: "))

# Ask the user for the symbol to fill the grid
symbol = input("Enter a symbol: ")

# Outer loop: Goes through each row
for x in range(rows):
    # Inner loop: Goes through each column in the current row
    for y in range(col):
        # Print the symbol without moving to a new line (end="" keeps it on the same line)
        print(symbol, end="")
    # After finishing one row, move to the next line
    print()
