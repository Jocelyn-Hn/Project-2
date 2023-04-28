from random import *


def main():
    option = input('What would you like to roll? \n'
                   'd100, d20, d12, d10, d8, d6, d4 \n'
                   'Options: Help, Quit \n'
                   '>> ')

    while option != 'Quit':
        number = int(input('How many times would you like to roll? \n'
                           '>> '))
        rolls = []

        if option == 'd100':
            for roll in range(number):
                rolls.append(randint(1, 101))

            print('Rolls:', ', '.join([str(roll) for roll in rolls]))
            print('Total:', sum(rolls))

        elif option == 'd20':
            for roll in range(number):
                rolls.append(randint(1, 21))

            print('Rolls:', ','.join([str(roll) for roll in rolls]))
            print('Total:', sum(rolls))

        elif option == 'd12':
            for roll in range(number):
                rolls.append(randint(1, 13))

            print('Rolls:', ','.join([str(roll) for roll in rolls]))
            print('Total:', sum(rolls))

        elif option == 'd10':
            for roll in range(number):
                rolls.append(randint(1, 11))

            print('Rolls:', ','.join([str(roll) for roll in rolls]))
            print('Total:', sum(rolls))

        elif option == 'd8':
            for roll in range(number):
                rolls.append(randint(1, 9))

            print('Rolls:', ','.join([str(roll) for roll in rolls]))
            print('Total:', sum(rolls))

        elif option == 'd10':
            for roll in range(number):
                rolls.append(randint(1, 11))

            print('Rolls:', ','.join([str(roll) for roll in rolls]))
            print('Total:', sum(rolls))

        elif option == 'Help':
            print('Roll options: d100, d20, d12, d10, d8, d6, d4. \n'
                  'Options: Help, Quit. \n'
                  '>> ')

        else:
            print('Please enter valid option.')

        break


if __name__ == '__main__':
    main()
