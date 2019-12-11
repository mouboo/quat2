#!/usr/bin/env python3
# graph.py
#

#optional to initialize Graph class
#gdict = {}

class Graph:
    """A graph data structure defining how rooms are connected.
    Arcs are one-way paths, edges are two-way paths."""
    
    def __init__(self, gdict = None):
        if gdict == None:
            gdict = {}
        self.g = gdict
        
    def show(self):
        print(self.g)
        
    def add_node(self, id):
        if not id in self.g:
            print("adding {}".format(id))
            self.g.update({ id : [] })
        else:
            print("Error: Room {} already exists".format(id))
            return
    
    def del_node(self, id):
        if id in self.g:
            del self.g[id]
        else:
            print("Error: No room with id {} to remove".format(id))
            return
    
    def add_arc(self, a, b):
        if a in self.g and b in self.g:
            self.g[a].append(b)
        else:
            print("Error: Can't add arc from {} to {}".format(a, b))
            
    def del_arc(self, a, b):
        if a in self.g and b in self.g[a]:
            self.g[a].remove(b)
        else:
            print("Error: Can't remove arc from {} to {}".format(a, b))


