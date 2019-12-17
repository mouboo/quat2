# parser.py

import actions

def parse_cmd(phrase, player):
    """ Main parsing function. Takes a user input string and executes a command.
        For now: commands must be on the form verb + noun"""
    
    p = player
    r = player.current_room

    cmd = lex(phrase)
    print("After lex: {}".format(cmd))
#    print(cmd[:1])
#    print(cmd[1:])
    
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


def lex(phrase):
    """ Takes an input phrase and returns a list of known words/group of words"""
    #Convert phrase to lower case
    phrase = phrase.lower()
    
    #Split string on whitespace into list of words
    raw_c = [word for word in phrase.split()]
    
    #Discard leading words that aren't a known verb
#    while not raw_c[0] in verbs:
#        del raw_c[0]
        
    #Check if there are more verbs, deal with error
#    vs = [v for v in raw_c if v in verbs]
#    if not len(vs) == 1:
#            print("Error: More than one verb/action")
#            return raw_c
            
    #Check if compound verb and nouns, replace in list
    for i in range(0,len(raw_c)-1):
        for j in range(0,len(raw_c)-1-i):
            compound = raw_c[i:len(raw_c)-j]
            c = ' '.join(compound)
            if c in known_words:
                raw_c.insert(i,c)
                for k in range(1,len(compound)+1):
                    del raw_c[i+1]
                    
    #Remove unknown words
    known_c = [c for c in raw_c if c in known_words]
    
    return known_c


synonyms = { 'go': ['g','walk','travel'],
             'look': ['l','examine','investigate','see']
            }

# (test words for now)
verbs = ['go', 'take', 'look', 'help', 'inventory', 'q', 'h', 'whoami', 'help', 'put on']
nouns = ['book', 'room', 'dagger', 'green bag', 'red rum','blue shirt']
preps = ['in','to','on','at']
rooms = ['bridge','north','kitchen'] # TODO: generate list from graph and alt. desc.
known_words = verbs + nouns + preps + rooms

