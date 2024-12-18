import time

# Function to print each letter with a delay
def print_letters_with_delay(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Move to the next line after printing all characters

# Add a delay before showing the prompt message
time.sleep(1)  # Delay for 1 second before displaying the prompt

# Get input from the user
user_input = "hello"

# Call the function with the user's input
print_letters_with_delay(user_input, delay=0.3)