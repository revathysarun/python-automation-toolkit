import random

def generate_password(length):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "!@#$%^&*_-"

    all_characters = letters + digits + symbols
    password = ""

    for i in range(length):
        password = password + random.choice(all_characters)

    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        if length < 6:
            print("Password length must be at least 6 characters.")
        else:
            print("Generated Password:", generate_password(length))
    except ValueError:
        print("Please enter a valid number.")
