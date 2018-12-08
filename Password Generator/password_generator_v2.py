import random

special_characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '&', '*', '(', ')', '.']

normal_characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def terminal_line():
    print('\033[31m' + '~~' * 50 + '\033[30m')


def password_generator():
    terminal_line()
    print('Take note that ↓\n'
          'Weak Password => 4 to 5 characters\n'
          'Medium Password => 6 to 11 characters\n'
          'Strong Password => 12 - 24 characters\n'
          'Impossible to BruteForce => 25 - 32 characters')
    terminal_line()

    password_size = str(input('Which size would you like to '
                              'the password be? [W/M/S/I]: ').upper().strip()[0])
    password_special = str(input('Would you like to your password '
                                 'contain special characters? [Y/N]: ').upper().strip()[0])

    password_length = 0
    new_password = list()

    def password_special_checker():
        if password_special == 'Y':
            while len(new_password) != password_length:
                new_password.append(random.choice(special_characters))
        elif password_special == 'N':
            while len(new_password) != password_length:
                new_password.append(random.choice(normal_characters))
        else:
            print('Type a motherfucking right value!')

    if password_size == 'W':
        password_length = random.randint(4, 5)
        password_special_checker()

    elif password_size == 'M':
        password_length = random.randint(6, 11)
        password_special_checker()

    elif password_size == 'S':
        password_length = random.randint(12, 24)
        password_special_checker()

    elif password_size == 'I':
        password_length = random.randint(25, 32)
        password_special_checker()

    else:
        print('Type a motherfucking right value!')

    new_password = "".join(new_password)
    print(f'Your new password is: {new_password}')

if __name__ == '__main__':
    password_generator()
