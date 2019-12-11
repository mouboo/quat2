# rooms.py

class Room:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
        
A = Room('Testroom A')
B = Room('Testroom B')