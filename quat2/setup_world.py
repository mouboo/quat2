#setup_world.py

import graph
import rooms
import persons
import items
import helpers

# Set up a world

g = graph.Graph()

# Start room
A = rooms.Room('Testroom A')
g.add_node(A)


# Second room
B = rooms.Room('Testroom B')
g.add_node(B)
g.add_arc(A, B)
g.add_arc(B, A)