from colorama import*
from data_create import *
def input_data():
    name, surname,phone, address = input_user_data()
    var = int(input(f'\nWhat shape do You prefer to save data?\n'
                    f'1 type: \n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{address}\n\n'
                    f'2 type: \n'
                    f'{name}; {surname}; {phone}; {address}\n\n'
                    f'Your choice: '))
    while var < 1 or var > 2:
        var = int(input(Fore.RED + 'Error!!! Try again: ' + Style.RESET_ALL))
    
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n'
                       f'{surname}\n'
                       f'{phone}\n'
                       f'{address}\n\n')    
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}; {surname}; {phone}; {address}\n\n')
    print(Fore.GREEN + f'Data was sucsessfully added in {var} file' + Style.RESET_ALL)


def print_data():
    print(Fore.GREEN + '1 File: ' + Style.RESET_ALL)
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        data_list = list()
        j = 0
        for i in range(len(data)):
            if data[i] == '\n':
                data_list.append(''.join(data[j:i]))
                j = i
        print(''.join(data_list))
    print(Fore.GREEN + '2 File: ' + Style.RESET_ALL)
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = list(file.readlines())
        print(''.join(data))


def delete_data():
    print('From what file do You want to remove data?')
    choice = int(input(Fore.YELLOW + 'Choose 1 or 2: ' + Style.RESET_ALL))
    while choice < 1 or choice > 2:
        choice = int(input(Fore.RED + 'Error!!! Try again: ' + Style.RESET_ALL))
    if choice == 1:

        with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            data = list(file.readlines())
            showed_data = list()
            for i, k in enumerate(data, 1):
                showed_data.append(i)
                showed_data.append(k)
            print(*showed_data)
        first = int(input(Fore.YELLOW + 'Enter the first string to delete: ' + Style.RESET_ALL))
        last = int(input(Fore.YELLOW + 'Enter the last string to delete with + 1: ' + Style.RESET_ALL))
        del data[first - 1 : last - 1]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.writelines(data)
            print(Fore.GREEN + 'Data was sucsessfully deleted' + Style.RESET_ALL)
    else:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
            data = list(file.readlines())
            print(''.join(data))
            showed_data = list()
            for i, k in enumerate(data, 1):
                showed_data.append(i)
                showed_data.append(k)
            print(*showed_data)
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            elem = int(input(Fore.YELLOW + 'Enter the number of string You want to delete: ' + Style.RESET_ALL))
            del data[elem -1 : elem + 1]
            file.writelines(data)
            print(Fore.GREEN + 'Data was sucsessfully deleted' + Style.RESET_ALL)                 
            
def change_data():
    print('In what file do You want to change data?')
    choice = int(input(Fore.YELLOW + 'Choose 1 or 2: ' + Style.RESET_ALL))
    while choice < 1 or choice > 2:
        choice = int(input(Fore.RED + 'Error!!! Try again: ' + Style.RESET_ALL))
    if choice == 1:
         with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            data = list(file.readlines())
            showed_data = list()
            for i, k in enumerate(data, 1):
                showed_data.append(i)
                showed_data.append(k)
            print(*showed_data)
         with open('data_first_variant.csv', 'w', encoding='utf-8') as file:   
            old_data = int(input(Fore.YELLOW + 'Enter the number of string You want to change: ' + Style.RESET_ALL))
            new_data = input(Fore.YELLOW + 'Enter new data: ' + Style.RESET_ALL)
            for i, k in enumerate(data, 1):
                if i == old_data:
                    file.writelines(f'{new_data} \n')
                else:
                    file.writelines(k)
            print(Fore.GREEN + 'Data was sucsessfully changed' + Style.RESET_ALL)
    else:
         with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
            data = list(file.readlines())
            print(''.join(data))
         with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
            data = file.read()
            old = input(Fore.YELLOW + 'Enter the word You want to change: ' + Style.RESET_ALL)
            new = input(Fore.YELLOW + 'Enter the new word: ' + Style.RESET_ALL)
            data = data.replace(old, new)
         with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(data)
            print(Fore.GREEN + 'Data was sucsessfully changed' + Style.RESET_ALL)

        