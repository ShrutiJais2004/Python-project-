def display_menu():
    print("\n===== CALCULATOR MENU =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


def get_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return None, None


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("Cannot divide by zero.")
        return None
    return a / b


def main():
    print("Welcome to Simple Calculator")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Exiting Calculator...")
            break

        num1, num2 = get_numbers()

        if num1 is None:
            continue

        if choice == "1":
            result = add(num1, num2)
            print("Result:", result)

        elif choice == "2":
            result = subtract(num1, num2)
            print("Result:", result)

        elif choice == "3":
            result = multiply(num1, num2)
            print("Result:", result)

        elif choice == "4":
            result = divide(num1, num2)
            if result is not None:
                print("Result:", result)

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()