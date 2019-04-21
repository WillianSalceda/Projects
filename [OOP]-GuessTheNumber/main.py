"""
This is a program that you got to guess the correct number using all (almost at least) features presented on your Udemy Course of automation of boring stuff
"""

from random import randint

class GuessTheNumber:
    def __init__(self, username, numberGenerated=randint(0, 9)):
        self.username = username
        self.numberGenerated = numberGenerated

        

    def guessingNumbers(self):
        username = self.username
        numberGenerated = self.numberGenerated
        

        print(f'So {username}, you probably know how it works, don\'t you?.\n'
              f'Well, anyway, if you don\'t, let me explain real quickly\n'
              f'Here you\'ll have 3 chances to guess the right number between 0 to 9.\n'
              f'YEAH! Seriously, it\'s all. I know, kind of disappointing (just like my english skills)...')
        # The line bellow can be deleted, it's just to inform the number for better debbuging.
        print(f'{self.numberGenerated} - Hey buddy, if you\'re reading that line, MAYBE YOU SHOULD READ THE FUCKING CODE, HUH?!')

        GUESSED_RIGHT = False
        NUMBER_OF_LIFES = 3
        while NUMBER_OF_LIFES != 0:            
            try:
                if NUMBER_OF_LIFES == 3:
                    numberGuessed = int(input(f'What is going to be your first number, {username}?\n'
                                              f'Hmmmm, let me guess... Probably '))
                elif NUMBER_OF_LIFES == 2:
                    numberGuessed = int(input(f'What is going to be your second number, {username}?\n'
                                              f'I\'ll go with '))
                else:
                    numberGuessed = int(input(f'Oooooh bloody hell... It\'s your last chance {username},   think a little bit...\m'
                                              f'Damn, maybe '))
                    
            except ValueError as valueError:
                print(f'You got an error: {valueError}\n'
                      f'This may be happening because you instead of putting a number, typed a word or letter.')

                print(f'Let\'s try again...\n'
                      f'But remember, if you type incorrectly this time, i will kick your but, okay?!\n'
                      f'Or maybe not, haven\'t codded it yet...')
                
                if NUMBER_OF_LIFES == 3:
                    numberGuessed = int(input(f'What is going to be your first number, {username}?\n'
                                              f'Hmmmm, let me guess... Probably '))
                elif NUMBER_OF_LIFES == 2:
                    numberGuessed = int(input(f'What is going to be your second number, {username}?\n'
                                              f'I\'ll go with '))
                else:
                    numberGuessed = int(input(f'Oooooh bloody hell... It\'s your last chance {username}, think a little bit...\n'
                                              f'Damn, maybe '))
            finally:
                if numberGuessed == numberGenerated:
                    if NUMBER_OF_LIFES == 3:
                        print(f'Congrats, on first attempt')
                        GUESSED_RIGHT = True
                        break
                    elif NUMBER_OF_LIFES == 2:
                        print(f'Congrats, on the second attempt')
                        GUESSED_RIGHT = True
                        break
                    elif NUMBER_OF_LIFES == 1:
                        print(f'Congrats, on your last attempt')
                        GUESSED_RIGHT = True
                        break
                else:
                    if NUMBER_OF_LIFES == 3:
                        print(f'Well, you still got 2 chances!\n'
                              f'Try again')
                    elif NUMBER_OF_LIFES == 2:
                        print(f'Time to think a little more, huh.\n'
                              f'Try again')
                    elif NUMBER_OF_LIFES == 1:
                        print(f'That was your last chance mate, too blame.')


            NUMBER_OF_LIFES -= 1

        if GUESSED_RIGHT == True:
            print(f'You got it right, it was: {self.numberGenerated}.')
        else:
            print(f'The right number was: {self.numberGenerated}.')

        

if __name__ == '__main__':
    game = GuessTheNumber(username=str(input('Hey, what is your name?\n'
                                            'Hi, my name is ')))
    game.guessingNumbers()
