# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password(n_letters, n_symbols, n_numbers):
    """Return a password string with the given mix of characters."""
    password_list = []
    for _ in range(n_letters):
        password_list.append(random.choice(letters))
    for _ in range(n_symbols):
        password_list.append(random.choice(symbols))
    for _ in range(n_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)
    return ''.join(password_list)

if __name__ == "__main__":
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))
    password = generate_password(nr_letters, nr_symbols, nr_numbers)
    print(f"Your password is: {password}")

