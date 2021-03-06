# parser.py

import itertools
import actions


### Words

verbdict = {'go' : ['walk', 'move'],
            'take' : ['get','grab'],
            'wear' : ['put on'],
            'look' : ['examine']
            }
preps = ['in','to','on','at']

def parse(phrase, player):
    """Takes a user input string and executes a command. """

    #Make a list of all known synonyms for all available actions,items, and rooms
    verbs = []
    for v in verbdict:
        verbs.append(v)
        verbs += verbdict[v]
    
    inventory = []
    for i in player.inventory:
        inventory.append(i.name)
        inventory.extend(i.synonyms)
    
    room_items = []
    for r in player.current_room.items:
        room_items.append(r.name)
        room_items.extend(r.synonyms)

    exits = []
    for e in player.current_room.exits.values():
        exits.extend(e)
    
    known_words = verbs + preps + inventory + room_items + exits
    
    #print("Verbs: {}".format(verbs))
    #print("Prepositions: {}".format(preps))
    #print("Inventory: {}".format(inventory))
    #print("Room items: {}".format(room_items))
    #print("Exits: {}".format(exits))

    #Convert phrase to lower case
    phrase = phrase.lower()
    
    #Split string on whitespace into list of words
    raw_p = [word for word in phrase.split()]
            
    #Check if compound verb and nouns, replace in list
    for i in range(0,len(raw_p)-1):
        for j in range(0,len(raw_p)-1-i):
            compound = raw_p[i:len(raw_p)-j]
            c = ' '.join(compound)
            if c in known_words:
                raw_p.insert(i,c)
                for k in range(1,len(compound)+1):
                    del raw_p[i+1]
                    
    #Remove unknown words
    cmd = [word for word in raw_p if word in known_words]
    
    # Analyze grammar: v=verb, n=noun, p=preposition, e=exit
    grammar = []
    for w in cmd:
        if w in verbs:
            grammar.append('v')
        elif w in inventory or w in room_items:
            grammar.append('n')
        elif w in preps:
            grammar.append('p')
        elif w in exits:
            grammar.append('e')
        else:
            print('Error: {} did not match a grammatic category'.format(w))
            
    print("Command components before binding: {}".format(cmd))
    print("Grammar: {}".format(grammar))
    
    #TODO: Sanity checks: One verb, determines function.
    
    if not grammar.count('v'):
        print("Error: multiple verbs")
        return
    
    if not grammar[0] == 'v':
        print("Error: verb not first")
        return

    #Go
    if cmd[0] == 'go' or cmd[0] in verbdict['go']:
        if 'e' in grammar:
            e_pos = grammar.index('e')
            print("Exit: {}".format(cmd[e_pos]))

        else:
            print("Error: no exit found")
        for x in player.current_room.exits:
            print(x)
        print("Current room: {}".format(player.current_room.name))
                

    #Look
    if cmd[0] == 'look' or cmd[0] in verbdict['look']:
        #TODO: deal with prepositions
        if len(cmd) == 1:
            player.look(player.current_room)
        elif len(cmd) == 2 and grammar[1] == 'n':
            word = cmd[1]
            matches = []
            for m in player.current_room.items + player.inventory:
                if cmd[1] == m.name or cmd[1] in m.synonyms:
                    matches.append(m)
            if len(matches) == 0:
                print("Don't know how to look at {}".format(cmd[1]))
            elif len(matches) > 1:
                print("Which {}?".format(cmd[1]))
            elif len(matches) == 1:
                player.look(matches[0])





    




