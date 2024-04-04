import random
import string

def generate_password(length, use_symbols=False, use_numbers=False, use_uppercase=False, use_lowercase=True):
    characters = ''
    if use_symbols:
        characters += string.punctuation
    if use_numbers:
        characters += string.digits
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase

    if not any([use_symbols, use_numbers, use_uppercase, use_lowercase]):
        print("Error: You must select at least one character type.")
        return None
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
#init