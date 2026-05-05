import random
import string

print("""
Advanced Password Generator
Author: Zahid Qureshi
""")

# Step 1: User inputs
length = int(input("Enter password length: "))
count = int(input("How many passwords do you want?: "))

use_upper = input("Include uppercase? (y/n): ").lower()
use_digits = input("Include numbers? (y/n): ").lower()
use_symbols = input("Include symbols? (y/n): ").lower()

# Step 2: Create character pool
characters = string.ascii_lowercase

if use_upper == 'y':
    characters += string.ascii_uppercase

if use_digits == 'y':
    characters += string.digits

if use_symbols == 'y':
    characters += string.punctuation

# Step 3: Generate password function
def generate_password():
    return ''.join(random.choice(characters) for _ in range(length))

# Step 4: Strength checker
def check_strength(password):
    if length >= 12:
        return "Strong"
    elif length >= 8:
        return "Medium"
    else:
        return "Weak"

# Step 5: Generate multiple passwords
print("\nGenerated Passwords:\n")

for i in range(count):
    pwd = generate_password()
    strength = check_strength(pwd)
    print(f"{i+1}. {pwd}  --> {strength}")

    # Save to file
    with open("passwords.txt", "a") as file:
        file.write(f"{pwd} --> {strength}\n")

print("\nPasswords saved to passwords.txt")
