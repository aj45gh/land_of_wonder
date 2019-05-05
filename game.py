import json


def start_game():
    pass


class Game(object):
    def __init__(self):
        pass

    def save(self):
        return json.dumps(self.__dict__)
