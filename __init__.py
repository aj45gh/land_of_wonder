import os
import sys
import json


def main():
    load_menu()


def load_menu():
    menu = {}
    if not os.path.isdir('./saves'):
        os.mkdir('saves')
    if list_saves():
        menu['CONTINUE'] = resume
    menu['NEW GAME'] = new_game
    menu['SETTINGS'] = settings
    menu['EXIT'] = exit_game
    print(', '.join(menu.keys()))
    while True:
        action = input()
        if action.upper() in menu.keys():
            break
    menu[action.upper()]()


def list_saves():
    return os.listdir('./saves')


def load_save(save):
    return json.load(open(save))


def new_game():
    while True:
        file_name = input('Enter the name for the new save file:\n')
        if not os.path.isfile(f'./saves/{file_name}.json'):
            break
        print('That save name is already in use.')
    open(f'./saves/{file_name}.json', 'w')


def resume():
    saves = ', '.join([save[:-5] for save in list_saves()])
    print(saves)


def settings():
    print('settings')


def exit_game():
    print('exit')
    sys.exit()


if __name__ == '__main__':
    main()
