# rooms.py

class Room:
    def __init__(self, name, desc='Not yet described.'):
        self.name = name
        self.synonyms = []
        self.desc = desc
        self.items = []
        self.exits = []

    
    def displaytext(self):
        print(self.name)
        print(self.desc)
        self.itemstext()
        
    def itemstext(self):
        #print("items: {}".format(self.items))
        print('You see: ', end='')
        for i in self.items:
            print(i, end =', ')
        print()
        

    def __str__(self):
        return self.name
        
