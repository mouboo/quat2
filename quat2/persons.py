#persons.py

import items

class Person:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []


class Player(Person):
    def __init__(self, name, current_room):
        super().__init__(name, current_room)
        self.inventory = [items.Book('red book'),
                          items.Dagger('obsidian dagger'),
                          items.Dagger('silver dagger')]
    
    def go(args):
        if args in self.currentroom.exits:
            self.currentroom = args
            print(self.currentroom.displaytext())
        else:
            print("error: can't go to {}".format(args))
    
    def look(args):
        args.displaytext()






class NonPlayableCharacter(Person):
    def __init__(self, name):
        super().__init__(name)