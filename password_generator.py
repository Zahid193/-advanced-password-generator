import string
import secrets
import argparse

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    if length < 4:
        raise ValueError("Password length should be at least 4")

    characters = ""
    
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character types selected!")

    password = []

    # Ensure at least one of each selected type
    if use_upper:
        password.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        password.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        password.append(secrets.choice(string.digits))
    if use_symbols:
        password.append(secrets.choice(string.punctuation))

    # Fill the rest
    for _ in range(length - len(password)):
        password.append(secrets.choice(characters))

    # Shuffle securely
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

def check_strength(password):
    length = len(password)
    types = 0

    if any(c.islower() for c in password):
        types += 1
    if any(c.isupper() for c in password):
        types += 1
    if any(c.isdigit() for c in password):
        types += 1
    if any(c in string.punctuation for c in password):
        types += 1

    if length >= 12 and types >= 3:
        return "Strong"
    elif length >= 8:
        return "Medium"
    else:
        return "Weak"

def main():
    parser = argparse.ArgumentParser(description="Advanced Password Generator")

    parser.add_argument("--length", type=int, default=12, help="Password length")
    parser.add_argument("--upper", action="store_true", help="Include uppercase")
    parser.add_argument("--lower", action="store_true", help="Include lowercase")
    parser.add_argument("--digits", action="store_true", help="Include digits")
    parser.add_argument("--symbols", action="store_true", help="Include symbols")
    parser.add_argument("--save", type=str, help="Save password to file")

    args = parser.parse_args()

    # Default: all enabled if nothing specified
    if not (args.upper or args.lower or args.digits or args.symbols):
        args.upper = args.lower = args.digits = args.symbols = True

    password = generate_password(
        args.length,
        args.upper,
        args.lower,
        args.digits,
        args.symbols
    )

    strength = check_strength(password)

    print("\nGenerated Password:", password)
    print("Strength:", strength)

    if args.save:
        with open(args.save, "a") as f:
            f.write(password + "\n")
        print(f"Saved to {args.save}")

if __name__ == "__main__":
    main()