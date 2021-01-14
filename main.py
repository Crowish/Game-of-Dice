#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 09:36:02 2021

@author: crow
"""

from handful_of_dice import Hand
from players import Player
from random import randrange

def play_hand():
    # implementation of single round of one player
    hand = Hand()
#    forcing dice values for testing
#    hand.dices['D1'].val = 1
#    hand.dices['D2'].val = 2
#    hand.dices['D3'].val = 3
#    hand.dices['D4'].val = 4
#    hand.dices['D5'].val = 5
#    hand.dices['D6'].val = 6
    hand.show_hand()
    print("Current score for this set:", hand.score())
    while not hand.all_stored():
        hand.store(input("Pick dices to store (numbers 1-6 separated by whitespace)\n"))
        print("\n\n\n...rerolling unstored dices...\n\n\n")
        hand.reroll_unstored()
        hand.show_hand()
        print("Current score for this set:", hand.score())
    print("\nAll dices stored")
    return hand.score()

        
if __name__ == '__main__':
    score = 0
    counter = 0
    print("Let's play Farkle!\n")
    while not counter:
        try:
            rounds = int(input("Set number of rounds: "))
            no_players = int(input("Set number of players: "))
            counter = rounds * no_players
        except ValueError:
            print("That wasn't really just number, was it...?"\
                  "\nCome on, try again\n")
    players = {}
    for i in range(1, no_players+1):
        players[i] = Player(i)
    print("\n\n")
    for i in range(counter):
        player_counter = i%no_players+1
        print("\n\n\n\n\n"+players[player_counter].get_name()+" playing!")
        if players[player_counter].is_cpu():
            players[player_counter].add_score_for_cpu(randrange(0,randrange(0,3000, 50), 50))
        else:
            players[player_counter].add_score(play_hand())
    print("\n\n")
    for player in players.values():
        player.get_total_score()
        
        
