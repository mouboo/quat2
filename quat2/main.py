#!/usr/bin/env python3
# main.py

#import graph
import rooms
import persons
import parser
import setup_world


def run():
    
    player = persons.Player('joe', rooms.A)
#    room = rooms.A

    while True:
        user_input = input('> ')
        parser.parse_cmd(user_input, player)
        
        
run()
    