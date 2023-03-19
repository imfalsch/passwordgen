import random
import string
import pyperclip

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
selection = int(input("Enter the number of the password you want to use: "))
selected_password = passwords[selection - 1]

# Copy the selected password to clipboard
pyperclip.copy(selected_password)
print(f"Selected password: {selected_password} (copied to clipboard)")
