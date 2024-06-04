def main():
    while True:  # to take infinite inputs
        try:
            # take input from the user
            expression = input("Enter an arithmetic expression (or 'quit' to exit): ")

            if expression.lower() == "quit":
                break

            result = eval(expression)
            print(f"Result: {result}")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
