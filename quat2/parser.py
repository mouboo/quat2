# parser.py

import actions


def parse_cmd(phrase, player):
    """ Main parsing function. Takes a user input string and executes a command.
        For now: commands must be on the form verb + noun"""
    
    p = player
    r = player.current_room
    
    cmd = lex(phrase)
    print("After lex: {}".format(cmd))
    
    if not cmd:
        print('No known words.')
        return
    
    if cmd[0] == 'go':
        actions.go(cmd[1])
    
    elif cmd[0] == 'h':
        s = "help"
    
    elif cmd[0] == 'whoami':
        s = p.name
    
    elif cmd[0] == 'look':
        s = p.current_room.name
    
    elif cmd[0] == 'inventory':
        s = ''
        for item in p.inventory:
            s += item + ', '
    
    else:
        s = "Invalid command."
        print(s)


def lex(phrase):
    """ Takes an input phrase and returns a list of known words"""
    phrase = phrase.lower()
    c = [word for word in phrase.split() if word in known_words]
    return c

# (test words for now)
verbs = ['go', 'look', 'help', 'inventory', 'q', 'h', 'whoami']
nouns = ['book', 'room', 'dagger', 'bag']
preps = ['in','to','on','at']
rooms = ['bridge','north','kitchen'] # TODO: generate list from graph and alt. desc.
known_words = verbs + nouns + preps + rooms

