#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 09:36:02 2021

@author: crow
"""
from game_guts import create_players, play_game
from printing import show_rules
        
if __name__ == '__main__':
    print("Let's play Farkle!\n")
    if input("Type \"rules\" to see rules or press ENTER to continue: ") == "rules":
        show_rules()
    players = create_players()
    play = True
    while play == True:
        play_game(players)
        if input("Play again? (yes/no)\n") == "yes":
            play = True
        else:
            play = False
