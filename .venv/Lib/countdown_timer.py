# Countdown Timer Program

# Import the time module to use the sleep() function, which adds a delay
import time

# Ask the user to enter a time in seconds
my_time = int(input("Enter your time in seconds: "))

# Use a loop to count down from the entered time to 0
# The range is reversed so it starts from my_time and goes down to 0
for x in reversed(range(0, my_time)):
    # Calculate the seconds part of the timer
    seconds = x % 60
    # Calculate the minutes part of the timer
    minutes = int(x / 60) % 60
    # Calculate the hours part of the timer
    hours = int(x / 3600)

    # Print the countdown in HH:MM:SS format
    # :02 means the number will always show with 2 digits (e.g., 01, 09, 10)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")

    # Pause the program for 1 second to make the countdown real-time
    time.sleep(1)

# When the countdown reaches 0, print a message
print("WAKEY WAKEY")
