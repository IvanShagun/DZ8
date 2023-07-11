from colorama import *
from logger import *

def interface():
    print(Fore.YELLOW + 'Hello! this is your Helpbot.' + Style.RESET_ALL)
    print('What operation do You prefer?\n'
           '1 - Add data\n'
           '2 - Show data\n'
           '3 - Delete data\n'
           '4 - CHange data\n')

    command = int(input(Fore.YELLOW + 'Your choice: ' + Style.RESET_ALL))

    while command < 1 or command > 4:
        command = int(input(Fore.RED + 'Error!!! Try again: ' + Style.RESET_ALL))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        delete_data()
    elif command == 4:
        change_data()

interface()