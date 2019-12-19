#!/usr/bin/env python3
# main.py

import setup_world
import persons
import parser


def run():
    
    roomset = setup_world.roomset
    player = persons.Player('joe', setup_world.startroom)

    while True:
        phrase = input('> ')
        parser.parse(phrase, player)
        
        
run()

    
