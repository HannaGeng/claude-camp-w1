import random
import string

def get_password_length():
    while True:
        try:
            length = int(input("Please enter the password length: "))

            if length < 6 or length > 10:
                print("密码需大于等于6位长度，但小于10位")
            else:
                return length

        except ValueError:
            print("Please enter a valid number.")


def generate_password(length):
    uppercase_letter = random.choice(string.ascii_uppercase)
    lowercase_letter = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special_character = random.choice("!@#$%^&*")

    required_characters = [
        uppercase_letter,
        lowercase_letter,
        digit,
        special_character
    ]

    all_characters = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        "!@#$%^&*"
    )

    remaining_length = length - len(required_characters)

    for _ in range(remaining_length):
        required_characters.append(random.choice(all_characters))

    random.shuffle(required_characters)

    password = "".join(required_characters)
    return password


password_length = get_password_length()
password = generate_password(password_length)

print(f"Your generated password is: {password}")
