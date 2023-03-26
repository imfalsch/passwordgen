import random
import string
import pyperclip

# MADE BY FALSCH

def generate_password(length):
    """Generates a strong password with the given length."""
    # Define character set
    charset = string.ascii_letters + string.digits + string.punctuation

    # Generate random password
    password = ''.join(random.choice(charset) for i in range(length))

    return password

# Generate 3 passwords with 10 characters each
passwords = []
for i in range(3):
    password = generate_password(10)
    passwords.append(password)
    pyperclip.copy(password)
    print(f"Password {i+1}: {password} (copied to clipboard)")

# Prompt the user to select a password
selection = int(input("Enter the number of the password you want to use (enter 0 to use the last copied password): "))

# Check if user wants to use the last copied password
if selection == 0:
    selected_password = pyperclip.paste()
    print(f"Selected password: {selected_password}")
else:
    selected_password = passwords[selection - 1]
    # Copy the selected password to clipboard
    pyperclip.copy(selected_password)
    print(f"Selected password: {selected_password} (copied to clipboard)")
    
# Copy the previous password to clipboard
previous_password = pyperclip.paste()
pyperclip.copy(previous_password)
print(f"Previous password: {previous_password} (copied to clipboard)")
