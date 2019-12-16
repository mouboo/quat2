#actions.py

def cmd_help(args):
    if h == 'go':
        print("'Go' usage: go [to] <direction>")
        
def go(args):
    print("You go to {}".format(args))
    
def inventory(args):
    s = ''
    for item in p.inventory:
        s += item + ', '
    
def look(args):
    pass