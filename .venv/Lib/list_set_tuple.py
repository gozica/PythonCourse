# Create a list
fruits = ["apple", "banana", "cherry"]

# Access items
print(fruits[0])  # Output: apple

# Add items
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# Change items
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']

# Remove items
fruits.remove("cherry")
print(fruits)  # Output: ['apple', 'blueberry', 'orange']

# Create a set
numbers = {1, 2, 3, 4, 4}  # Duplicate '4' will be removed

# Access items (you can't access by index because it's unordered)
print(numbers)  # Output: {1, 2, 3, 4}

# Add items
numbers.add(5)
print(numbers)  # Output: {1, 2, 3, 4, 5}

# Remove items
numbers.remove(3)
print(numbers)  # Output: {1, 2, 4, 5}

# Create a tuple
colors = ("red", "green", "blue")

# Access items
print(colors[0])  # Output: red

# You can't change or add items
# colors[1] = "yellow"  # This will cause an error

# Tuples can have duplicates
numbers = (1, 2, 2, 3)
print(numbers)  # Output: (1, 2, 2, 3)

# Length of a tuple
print(len(colors))  # Output: 3
