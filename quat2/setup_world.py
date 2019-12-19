#setup_world.py

import rooms
import items

#Room A
A = rooms.Room('Testroom A')

#Room B
B = rooms.Room('Testroom B')
B.items = [items.Item('dagger'),items.Item('blue shirt'), items.Item('red rum')]

#Room C
C = rooms.Room('Testroom C')

#Room D
D = rooms.Room('Testroom D')

#Exits
A.exits = [B,C]
B.exits = [A,D]
C.exits = [B,D]
D.exits = [A,B,C,D]

#Set of rooms in game
roomset = {A,B,C,D}

#Startroom
startroom = B