#concession stand program

# The menu is like a list of foods you can buy, with their prices
menu = {
    "pizza": 3.00,       # Pizza costs $3.00
    "nachos": 4.50,      # Nachos cost $4.50
    "popcorn": 6.00,     # Popcorn costs $6.00
    "fries": 2.50,       # Fries cost $2.50
    "chips": 1.00,       # Chips cost $1.00
    "pretzel": 3.50,     # Pretzel costs $3.50
    "soda": 3.00,        # Soda costs $3.00
    "lemonade": 4.25     # Lemonade costs $4.25
}

# The cart is like your shopping bag. It starts empty.
cart = []

# This keeps track of how much money everything in the cart costs. Start at $0.
total = 0

# Print the menu so the user knows what they can buy
print("--------- MENU ---------")  # This is the menu header
for key, value in menu.items():   # Go through each food and price in the menu
    #key: gets the name of the food (like "pizza").
    #value: gets the price of that food (like 3.00).
    print(f"{key:10}: ${value:.2f}")  # Print the food name and its price, nicely lined up
print("------------------------")  # Print a line to separate the menu from what's next

# Let the user pick foods until they want to quit
while True:
    # Ask the user to choose a food or type 'q' to quit
    food = input("Select an item (q to quit): ").lower()  # Lowercase ensures input matches menu keys
    if food == "q":  # If the user types 'q', stop asking for more food
        break
    elif menu.get(food) is not None:  # Check if the food is in the menu
        cart.append(food)  # Add the food to the cart
    else:
        print("Sorry, that's not on the menu!")  # If food isn't in the menu, let them know

# Print the foods the user added to their cart
print("------ YOUR ORDER ------")
for food in cart:  # Go through each food in the cart
    total += menu.get(food)  # Add the price of that food to the total
    print(food, end=" ")  # Print each food on the same line

print()  # Print a blank line after the list of food items
print(f"Total is: ${total:.2f}")  # Print how much everything in the cart costs
