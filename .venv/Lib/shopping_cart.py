# Create two empty lists to store the names of foods and their prices
foods = []
prices = []

# Start with a total of $0
total = 0

# Start a loop to keep asking the user for foods and prices
while True:
    # Ask the user to enter the name of a food item
    food = input("Enter a food to buy (q to quit): ")

    # Check if the user typed "q" (to quit)
    if food.lower() == "q":  # .lower() makes sure "Q" or "q" both work
        break  # Stop the loop if the user wants to quit

    # If the user didn't quit, ask for the price of the food
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        # Convert the price to a decimal number (float) so we can calculate later

        foods.append(food)  # Add the food to the list of foods
        prices.append(price)  # Add the price to the list of prices

# Print a header for the shopping cart
print("----- YOUR CART -----")

# Loop through the list of foods and print each food on the same line
for food in foods:
    print(food, end=" ")  # end=" " makes all the foods print on the same line

# Add up all the prices to calculate the total
for price in prices:
    total += price  # Add each price to the total

# Print a blank line for better formatting
print()

# Print the total cost of everything in the cart
print(f"Your total is: ${total}")