#setup_world.py

import rooms
import items

#Rooms
A = rooms.Room('Testroom A')
B = rooms.Room('Testroom B')
C = rooms.Room('Testroom C')
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