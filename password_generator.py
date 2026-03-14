import random
import string


def display_menu():
    print("\n=== PASSWORD GENERATOR ===")
    print("1. Basic Password")
    print("2. Strong Password")
    print("3. Exit")


def get_length():
    while True:
        try:
            length = int(input("Enter password length: "))
            if length > 0:
                return length
            else:
                print("Enter length greater than 0")
        except:
            print("Enter a valid number")


def generate_basic(length):
    chars = string.ascii_letters + string.digits
    password = "".join(random.choice(chars) for _ in range(length))
    return password


def generate_strong(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for _ in range(length))
    return password


def main():
    while True:
        display_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            length = get_length()
            pwd = generate_basic(length)
            print("Generated Password:", pwd)

        elif choice == "2":
            length = get_length()
            pwd = generate_strong(length)
            print("Generated Strong Password:", pwd)

        elif choice == "3":
            print("Exit...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()