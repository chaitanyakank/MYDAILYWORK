import random
import string

def generate_password(length, use_uppercase, use_digits, use_specials):
    # Character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ""
    digits = string.digits if use_digits else ""
    specials = string.punctuation if use_specials else ""

    # Combine selected pools
    all_characters = lower + upper + digits + specials

    if len(all_characters) == 0:
        return "Error: No character sets selected."

    # Ensure at least one character from each selected pool
    password = []
    if use_uppercase:
        password.append(random.choice(upper))
    if use_digits:
        password.append(random.choice(digits))
    if use_specials:
        password.append(random.choice(specials))

    # Fill the remaining length
    password += random.choices(all_characters, k=length - len(password))

    # Shuffle to randomize
    random.shuffle(password)

    return ''.join(password)

# User input
length = int(input("Enter password length: "))
use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == "yes"
use_digits = input("Include numbers? (yes/no): ").strip().lower() == "yes"
use_specials = input("Include special characters? (yes/no): ").strip().lower() == "yes"

# Generate and display password
password = generate_password(length, use_uppercase, use_digits, use_specials)
print("Generated Password:", password)
