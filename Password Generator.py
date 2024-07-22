import random


def pass_gen():
    print("Hello! What is your name?")
    name = input("Enter your name: ")
    print("Welcome, " + name + "!")

    while True:
        try:
            pass_len = int(input("Please enter the length of the password: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    UPPERCASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    LOWERCASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    SPECIAL = ['@', '#', '$', '=', ':', '?', '.', '/', '|', '~', '>', '*', '<']

    combination = UPPERCASE + LOWERCASE + DIGITS + SPECIAL

    if pass_len > 0:
        password = "".join(random.sample(combination, pass_len))
        print("Generated password: " + password)
    else:
        print("Password length must be greater than 0.")


while True:
    pass_gen()
    selection = input("Would you like to generate another password? (Yes or No): ").lower()

    if selection != 'yes':
        break

print("Thank you for using the password generator!")
