import sqlite3
import winsound
import os
import sys

from time import sleep


def lines(letter, length):
    print(f'{letter}' * length)


def fake_loading(message, timer):
    print(f'{message}', end='')
    sleep(0.5)

    for index in range(0, 3):
        print('.', end='')
        sleep(timer)
        sys.stdout.flush()


class Manager:
    def __init__(self):
        self.name = ''
        self.age = ''
        self.phone = ''
        self.address = ''

    def create(self):
        os.system('cls')

        create_running = True
        while create_running:
            lines('~', 50)
            print(f"{'ADD A NEW CONTACT':^50}")
            lines('~', 50)

            db = sqlite3.connect('connection.sqlite3')
            cursor = db.cursor()
            cursor.execute("SELECT Name FROM contacts")
            all_names = cursor.fetchall()

            self.name = str(input('Name: ').strip().title())
            sleep(0.30)
            if self.name == '':
                keep_creating = input(f'You haven\'t typed any name, are you sure you want to '
                                      f'continue? [Y/N]: ').strip().upper()
                if keep_creating == 'Y':
                    pass
                else:
                    self.menu()

            for name in all_names:
                if self.name in name:
                    keep_creating = input(f'There is already the name {name} in database. Do you want to '
                                          f'continue? [Y/N]: ').strip().upper()
                    if keep_creating == 'Y':
                        break
                    else:
                        self.menu()
                else:
                    continue

            sleep(0.30)
            self.age = str(input('Age: ').strip())
            sleep(0.30)
            self.phone = str(input('Phone: ').strip())
            sleep(0.30)
            self.address = str(input('Address: ').strip().title())
            sleep(0.30)

            db = sqlite3.connect('connection.sqlite3')
            cursor = db.cursor()
            cursor.execute('''INSERT INTO contacts\
                           (Name, Age, Phone, Address)VALUES(?,?,?,?)''',
                           (self.name, self.age, self.phone, self.address))
            db.commit()

            print('NEW CONTACT ADDED TO DATABASE')
            sleep(1.0)

            keep_running = input('Do you want to add more contacts? [Y/N]: ').upper()

            if keep_running == 'N':
                db.close()
                create_running = False
                self.menu()
            else:
                continue

    def read(self):
        try:
            os.system('cls')

            db = sqlite3.connect('connection.sqlite3')
            cursor = db.cursor()

            lines('~', 50)
            print(f"{'CONTACTS':^50}")
            lines('~', 50)
            sleep(0.3)

            cursor.execute('SELECT Name, Age, Phone, Address FROM contacts')
            all_contacts = cursor.fetchall()

            types_of_data = ['Name:', 'Age:', 'Phone:', 'Address:']

            for contact in all_contacts:
                data_index = 0

                for item in contact:
                    if item.strip() == '':
                        print(f'{types_of_data[data_index]:^10} {"NULL":^25}', end=' ')
                    else:
                        print(f'{types_of_data[data_index]:^10} {item:^25}', end=' ')
                    data_index += 1

                sleep(0.15)
                print(end='\n')

            print('\nNO MORE RESULTS!\n')

            read_continue = str(input('Press any key to continue'))
            self.menu()
        except:
            print('Couldn\'t read any contacts. You probably haven\'t any yet!')
            print('Try adding at least one first.')
            fake_loading('BACK TO MENU', 1.5)
            self.menu()

    def update(self):
        os.system('cls')

        lines('~', 50)
        print(f"{'UPDATE CONTACTS':^50}")
        lines('~', 50)

        db = sqlite3.connect('connection.sqlite3')
        cursor = db.cursor()
        cursor.execute("SELECT Name FROM contacts")
        all_names = cursor.fetchall()

        name_to_update = str(input('Type the name of the contact you want to update: ').strip().title())

        for name in all_names:
            if name_to_update in name:
                confirm_update = input(f'YOU WANT TO UPDATE {name_to_update}? [Y/N]: ').strip().upper()
                if confirm_update == 'Y':

                    self.name = str(input('Name: ').strip().title())
                    if self.name != '' and self.name != name:
                        cursor.execute("UPDATE contacts SET Name = ? WHERE Name = ?",
                                       (self.name, name_to_update))
                    else:
                        print('ERROR - NEW NAME IS IN BLANK OR THE SAME AS BEFORE')
                        fake_loading('BACK TO MENU', 0.5)
                        db.close()
                        self.menu()
                    sleep(0.30)
                    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
                    self.age = str(input('Age: ').strip().title())
                    cursor.execute("UPDATE contacts SET Age = ? WHERE Name = ?",
                                   (self.age, self.name))
                    if self.age != '':
                        cursor.execute("UPDATE contacts SET Age = ? WHERE Name = ?",
                                       (self.age, self.name))
                    else:
                        print('ERROR - NEW AGE IS IN BLANK')
                        update_continue = input('DO YOU WANT TO CONTINUE? [Y/N]: ').strip().upper()

                        if update_continue == 'Y':
                            pass
                        else:
                            fake_loading('BACK TO MENU', 0.5)
                            db.close()
                            self.menu()
                    sleep(0.30)
                    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
                    self.phone = str(input('Phone: ').strip().title())
                    cursor.execute("UPDATE contacts SET Phone = ? WHERE Name = ?",
                                   (self.phone, self.name))
                    if self.phone != '':
                        cursor.execute("UPDATE contacts SET Phone = ? WHERE Name = ?",
                                       (self.phone, self.name))
                    else:
                        print('ERROR - NEW PHONE IS IN BLANK')
                        update_continue = input('DO YOU WANT TO CONTINUE? [Y/N]: ').strip().upper()

                        if update_continue == 'Y':
                            pass
                        else:
                            fake_loading('BACK TO MENU', 0.5)
                            db.close()
                            self.menu()
                    sleep(0.30)
                    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
                    self.address = str(input('Address: ').strip().title())
                    cursor.execute("UPDATE contacts SET Address = ? WHERE Name = ?",
                                   (self.address, self.name))
                    if self.address != '':
                        cursor.execute("UPDATE contacts SET Address = ? WHERE Name = ?",
                                       (self.address, self.name))
                    else:
                        print('ERROR - NEW ADDRESS IS IN BLANK')
                        update_continue = input('DO YOU WANT TO CONTINUE? [Y/N]: ').strip().upper()

                        if update_continue == 'Y':
                            pass
                        else:
                            fake_loading('BACK TO MENU', 0.5)
                            db.close()
                            self.menu()
                    sleep(0.30)
                    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
                    print('USER UPDATED FROM DATABASE!')
                    fake_loading('BACK TO MENU', 0.5)
                    db.commit()
                    db.close()
                    self.menu()

                else:
                    fake_loading('BACK TO MENU', 0.5)
                    db.close()
                    self.menu()
            else:
                continue

    def delete(self):
        os.system('cls')

        lines('~', 50)
        print(f"{'DELETE CONTACTS':^50}")
        lines('~', 50)

        db = sqlite3.connect('connection.sqlite3')
        cursor = db.cursor()
        cursor.execute("SELECT Name FROM contacts")
        all_names = cursor.fetchall()

        name_to_delete = str(input('Type the name of the contact you want to delete: ').strip().title())
        for name in all_names:
            if name_to_delete in name:
                confirm_delete = input(f'YOU WANT TO DELETE {name_to_delete}? [Y/N]: ').strip().upper()
                if confirm_delete == 'Y':
                    cursor.execute("DELETE FROM contacts WHERE Name = ?", (name_to_delete,))

                    print('USER DELETED FROM DATABASE!')
                    fake_loading('BACK TO MENU', 0.5)
                    db.commit()
                    self.menu()
                else:
                    fake_loading('BACK TO MENU', 0.5)
                    self.menu()
            else:
                continue

        print('NAME NOT FOUND ON DATABASE!')
        fake_loading('BACK TO MENU', 0.5)
        self.menu()

    def exit(self):
        confirm = str(input('ARE YOU SURE YOU WANT TO QUIT? [Y/N]: ').strip().upper())
        if confirm == 'Y':
            pass
        else:
            fake_loading('\nBACK TO MENU', 0.5)
            self.menu()

    def menu(self):
        os.system('cls')

        print('')
        winsound.Beep(2000, 200)

        lines('~', 50)
        print(f"{'MENU':^50}")
        lines('~', 50)

        options = ['1 - CREATE',
                   '2 - READ',
                   '3 - UPDATE',
                   '4 - DELETE',
                   '5 - EXIT']

        for option in options:
            print(option)
            sleep(0.05)
            if option == '5 - EXIT':
                print('')

        choose_option = int(input('Select an option: '))

        if choose_option == 1:
            self.create()

        elif choose_option == 2:
            self.read()

        elif choose_option == 3:
            self.update()

        elif choose_option == 4:
            self.delete()

        elif choose_option == 5:
            self.exit()
        else:
            print('SELECT A VALID OPTION')
            sleep(1.5)

    def main(self):
        os.system('cls')

        if os.path.isfile("connection.sqlite3"):
            db = sqlite3.connect("connection.sqlite3")
            sleep(0.5)
            winsound.Beep(2000, 200)
            fake_loading('Connecting to database', 0.5)

            print()
            print('DATABASE CONNECTED!')
            sleep(1)
            self.menu()

        else:
            print('COULDN\'T CONNECT TO DATABASE')
            print('')
            sleep(0.5)
            winsound.Beep(2000, 200)

            print('CREATING NEW CONNECTION TO DATABASE')
            open("connection.sqlite3", "x+")
            db = sqlite3.connect("connection.sqlite3")
            sleep(1)

            print('CONNECTION CREATED!')
            sleep(1)
            print('DATABASE CONNECTED!')
            sleep(1.5)

            self.menu()

            cursor = db.cursor()
            cursor.execute('''CREATE TABLE contacts\
                           (Name TEXT, Age TEXT, phone TEXT, ADDRESS TEXT)''')


if __name__ == '__main__':
    Manager().main()

