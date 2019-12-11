#persons.py

class Person:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []


class Player(Person):
    def __init__(self, name, current_room):
        super().__init__(name, current_room)
        self.inventory = ["stuff","more stuff"]

class NonPlayableCharacter(Person):
    def __init__(self, name):
        super().__init__(name)