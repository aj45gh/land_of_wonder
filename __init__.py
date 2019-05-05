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
    menu['NEW'] = new_game
    menu['SETTINGS'] = settings
    menu['EXIT'] = sys.exit
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
    print('new game')
    pass


def resume():
    print('continue')
    pass


def settings():
    print('settings')
    pass


if __name__ == '__main__':
    main()
