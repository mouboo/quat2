# rooms.py

class Room:
    def __init__(self, name, desc='Not yet described.', exits=[]):
        self.name = name
        self.desc = desc
        self.exits = exits

    
    def __str__(self):
        return self.name
        
