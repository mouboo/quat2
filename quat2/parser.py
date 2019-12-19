# parser.py

import actions

### Words

verbs = ['go', 'take', 'look', 'help', 'inventory', 'q', 'h', 'whoami', 'help', 'put on', 'put']
#nouns = ['book', 'room', 'dagger', 'green bag', 'red rum','blue shirt']
preps = ['in','to','on','at']

def parse(phrase, player):
    """Takes a user input string and executes a command. """

    exits = [e.name.lower() for e in player.current_room.exits]
    inventory = [i.name.lower() for i in player.inventory]
    room_items = [ri.name.lower() for ri in player.current_room.items]
    known_words = verbs + preps + exits + inventory + room_items
    
    print("Inventory: {}".format(inventory))
    print("Room items: {}".format(room_items))
    print("Exits: {}".format(exits))


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
            
    #TODO: Bind cmd words to functions and objects
    
    print("Command components: {}".format(cmd))
    print("Grammar: {}".format(grammar))






