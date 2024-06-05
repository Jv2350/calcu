import random


def random_password(length):
    capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_letters = "abcedfghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    special_letters = '~!@#$%^&*()_+{}:"<>?,./;'

    all_characters = capital_letters + small_letters + numbers + special_letters

    password = ""
    for i in range(length):
        character = random.choice(all_characters)
        password += character

    return password


def main():
    try:
        length_of_password = int(input("Enter the length of the password: "))
        if length_of_password <= 0:
            print("Password length must be greater than zero")
            return

        password = random_password(length_of_password)
        print("Generated Password:", password)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
