#items.py

class Item():
    def __init__(self, name):
        self.name = name
        self.synonyms = []
        self.weight = 1
        self.container = False

    def __str__():
        return self.name

class Dagger(Item):
    def __init__(self, name):
        super().__init__(name)
        self.synonyms = ['dagger','knife','weapon']
        self.weapon = True
        self.attack = 5
        
class Book(Item):
    def __init__(self, name):
        super().__init__(name)
        self.synonyms = ['book','tome']
        self.weapon = True
        self.attack = 1

class Ring(Item):
    def __init__(self, name):
        super().__init__(name)
        self.synonyms = ['ring']
        
        
