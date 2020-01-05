#setup_world.py

import rooms
import items
import persons

#Room A
A = rooms.Room('Testroom A')

#Room B
B = rooms.Room('Testroom B')
B.desc = 'Testroom B is kind of an empty test room.'
B.items = [items.Dagger('rusty dagger'), items.Ring("white gold ring")]

#Room C
C = rooms.Room('Testroom C')

#Room D
D = rooms.Room('Testroom D')

#Exits
A.exits = {B : ['forest','east'], C : ['river','north']}
B.exits = {A : ['house','west'], D : ['shed','south']}
C.exits = [B,D]
D.exits = [A,B,C,D]

#Set of rooms in game
roomset = {A,B,C,D}

#Startroom
startroom = B