# Simple Calculator Program

# Ask the user to enter an operator (+, -, *, or /)
operator = input("Enter an operator (+ - * /): ")

# Ask the user to enter the first number (convert it to a decimal with float)
num1 = float(input("Enter the 1st number: "))

# Ask the user to enter the second number (convert it to a decimal with float)
num2 = float(input("Enter the 2nd number: "))

# Check if the operator is "+" (addition)
if operator == "+":
   result = num1 + num2  # Add the two numbers
   print(round(result, 3))  # Print the result rounded to 3 decimal places

# Check if the operator is "-" (subtraction)
elif operator == "-":
   result = num1 - num2  # Subtract the second number from the first
   print(round(result, 3))  # Print the result rounded to 3 decimal places

# Check if the operator is "*" (multiplication)
elif operator == "*":
   result = num1 * num2  # Multiply the two numbers
   print(round(result, 3))  # Print the result rounded to 3 decimal places

# Check if the operator is "/" (division)
elif operator == "/":
   result = num1 / num2  # Divide the first number by the second
   print(round(result, 3))  # Print the result rounded to 3 decimal places

# If the operator is none of the above, it's invalid
else:
   print(f"{operator} is not a valid operator")  # Tell the user the operator is invalid
