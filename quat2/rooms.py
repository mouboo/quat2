# rooms.py

class Room:
    def __init__(self, name, desc='Not yet described.', items=[], exits=[]):
        self.name = name
        self.desc = desc
        self.items = items
        self.exits = exits

    
    def displaytext(self):
        print(self.name)
        print(self.desc)
        itemstext()
        
    def itemstext(self):
        print('You see: ', end='')
        for i in items:
            print(i + ' ', end='')

    
    def __str__(self):
        return self.name
        
