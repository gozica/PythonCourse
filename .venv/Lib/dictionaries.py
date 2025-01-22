# Dictionary = A collection of {key:value} pairs
#              Ordered (since Python 3.7), changeable, and does not allow duplicates

# Create a dictionary called 'capitals' with countries as keys and their capitals as values
capitals = {
    "USA": "Washington D.C",  # Key: "USA", Value: "Washington D.C"
    "India": "New Delhi",     # Key: "India", Value: "New Delhi"
    "China": "Beijing",       # Key: "China", Value: "Beijing"
    "Russia": "Moscow"        # Key: "Russia", Value: "Moscow"
}

# Get the capital of "USA" using the dictionary's .get() method
print(capitals.get("USA"))  # Output: "Washington D.C"

# Check if the key "Japan" exists in the dictionary
if capitals.get("Japan"):
    print("That capital exists")  # This will not run because "Japan" is not in the dictionary
else:
    print("That capital does not exist")  # Output: "That capital does not exist"

# Add or update a key-value pair in the dictionary
capitals.update({"Germany": "Berlin"})  # Adds "Germany": "Berlin" to the dictionary
print(capitals)  # Prints the updated dictionary with "Germany" included

# Remove a key-value pair from the dictionary
capitals.pop("China")  # Removes "China": "Beijing" from the dictionary
print(capitals)  # Prints the dictionary without "China"

# Clear all key-value pairs from the dictionary
capitals.clear()  # Empties the entire dictionary
print(capitals)  # Output: {} (an empty dictionary)
