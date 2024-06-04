def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2


def main():
    print(
        """Simple calculator
    Choose Operation: 
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division"""
    )

    count = 0
    while count < 10:
        try:
            choice = input("Enter choice (1/2/3/4) or 'quit' to exit: ")
            if choice.lower() == "quit":
                break

            if choice not in ("1", "2", "3", "4"):
                print("Invalid input. Please enter valid choice.")
                continue

            num1 = float(input("Enter 1st number: "))
            num2 = float(input("Enter 2nd number: "))

            if choice == "1":
                result = add(num1, num2)
                operator = "+"

            elif choice == "2":
                result = sub(num1, num2)
                operator = "-"

            elif choice == "3":
                result = mul(num1, num2)
                operator = "*"

            elif choice == "4":
                result = div(num1, num2)
                operator = "/"

            print(f"The result of {num1} {operator} {num2} is {result}")

            count += 1
            if count == 10:
                print("\nMaximum number of calculations reached.")
                break

        except Exception as e:
            print(f"Error: {e}")

        input("Press Enter to continue or type 'quit' to exit: ")
        if choice.lower() == "quit":
            break


if __name__ == "__main__":
    main()
