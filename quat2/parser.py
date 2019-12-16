# parser.py

import actions

def parse_cmd(phrase, player):
    """ Main parsing function. Takes a user input string and executes a command.
        For now: commands must be on the form verb + noun"""
    
    p = player
    r = player.current_room

    cmd = lex(phrase)
    print("After lex: {}".format(cmd))
    print(cmd[:1])
    print(cmd[1:])
    
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
    """ Takes an input phrase and returns a list of known words"""
    phrase = phrase.lower()
    c = [word for word in phrase.split() if word in known_words]
    return c

synonyms = { 'go': ['g','walk','travel'],
             'look': ['l','examine','investigate','see']
            }

# (test words for now)
verbs = ['go', 'look', 'help', 'inventory', 'q', 'h', 'whoami', 'help']
nouns = ['book', 'room', 'dagger', 'bag']
preps = ['in','to','on','at']
rooms = ['bridge','north','kitchen'] # TODO: generate list from graph and alt. desc.
known_words = verbs + nouns + preps + rooms

