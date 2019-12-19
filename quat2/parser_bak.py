# parser.py

import actions

def parse_cmd(phrase, player):
    """ Main parsing function. Takes a user input string and executes a command.
        For now: commands must be on the form verb + noun"""
    
    p = player
    r = player.current_room

    known_words = verbs + nouns + preps + exits + p.inventory + r.items


    # Make list of known keywords
    cmd = lex(phrase, known_words)
    print("After lex: {}".format(cmd))
    
    # Make list of grammar
    grammar = gram(cmd, p)
    print("After grammar: {}".format(grammar))
    

    if not cmd:
        print('No known words.')
        return
    
    if cmd[0] in 'go':
        
        print("You go to {}".format(cmd[1]))
            
    elif cmd[0] == 'whoami':
        s = p.name
    
    elif cmd[0] == 'look':
        print(p.current_room.name)
        print('exits: {}'.format(r.exits))
    
    elif cmd[0] == 'inventory':
        pass
    
    else:
        s = "Invalid command."
        print(s)


def lex(phrase, known_words):
    """ Takes an input phrase and returns a list of known words/group of words"""
    #Convert phrase to lower case
    phrase = phrase.lower()
    
    #Split string on whitespace into list of words
    raw_p = [word for word in phrase.split()]
    
    #Discard leading words that aren't a known verb
#    while not raw_p[0] in verbs:
#        del raw_p[0]
        
    #Check if there are more verbs, deal with error
#    vs = [v for v in raw_p if v in verbs]
#    if not len(vs) == 1:
#            print("Error: More than one verb/action")
#            return raw_p
            
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
    known_p = [word for word in raw_p if word in known_words]
    
    return known_p

def gram(cmd,p):
    g = []
    for w in cmd:
        if w in verbs:
            g.append('v')
        elif w in nouns or w in p.inventory or w in p.current_room.items:
            g.append('n')
        elif w in preps:
            g.append('p')
        elif w in p.current_room.exits:
            g.append('r')
        else:
            print('Error: {} did not match a grammatic category'.format(w))
    return g

synonyms = { 'go': ['g','walk','travel'],
             'look': ['l','examine','investigate','see']
            }

# (test words for now)
verbs = ['go', 'take', 'look', 'help', 'inventory', 'q', 'h', 'whoami', 'help', 'put on', 'put']
nouns = ['book', 'room', 'dagger', 'green bag', 'red rum','blue shirt']
preps = ['in','to','on','at']
exits = ['bridge','north','kitchen']


