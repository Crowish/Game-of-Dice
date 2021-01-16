#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 10:13:48 2021

@author: crow
"""

from handful_of_dice import Hand
from players import Player
from random import randrange

def play_hand():
    # implementation of single round of one player
    hand = Hand()
#    forcing dice values for testing
#    hand.dices['D1'].val = 2
#    hand.dices['D2'].val = 3
#    hand.dices['D3'].val = 4
#    hand.dices['D4'].val = 6
#    hand.dices['D5'].val = 3
#    hand.dices['D6'].val = 2
    hand.show_hand()
    rerolled = hand.return_unstored()
    while not hand.all_stored():
        if len(rerolled) == 6 and hand.reroll_valid(rerolled) == 0:
            print("Tough luck! No scoring dice here...\n"\
                  "Your turn is lost")
            return 0
            
        if hand.reroll_valid(rerolled) == 0 and len(rerolled) != 0:
            print("Reroll did not produce any score\n"\
                  "Your points are lost\n"\
                  "End of turn")
            return 0
        elif len(rerolled) > 0:
            stored = hand.store(input("Pick dice to store (numbers 1-6 separated by whitespace)\n"))
            rerolled = hand.reroll_unstored()
            curr_score = hand.update_score(stored)
            print("Current score for stored:", curr_score)
        else:
            stored = hand.store(input("Pick dice to store (numbers 1-6 separated by whitespace)\n"))
            rerolled = hand.reroll_unstored()
            curr_score = hand.update_score(stored)      
        hand.show_hand()      
    print("\nAll dice stored,", curr_score, "points added to player's total score")
    return curr_score

def create_players():
    no_players = 0
    while not no_players:
        try:
            no_players = int(input("\nSet number of players: "))
        except ValueError:
            print("That wasn't really just a number, now was it...?"\
                  "\nCome on, try again\n")
    players = {}
    for i in range(1, no_players+1):
        players[i] = Player(i)
    return players
    
    
def play_game(players):
    highest_score = 0
    goal = 0
    i = 0
    no_players = len(players)
    while not goal:
        try:
            goal = int(input("\nSet goal: "))
        except ValueError:
            print("That wasn't really just a number, now was it...?"\
                  "\nCome on, try again\n")
    while highest_score < goal:
        if i%no_players == 0:
            print("\n\n\n\n################### ROUND",i//no_players+1,"###################")
        for j in range(no_players):
            player_counter = i%no_players+1
            print("\n\n\n\n\n"+players[player_counter].get_name()+" playing!")
            if players[player_counter].is_cpu():
                players[player_counter].add_score_for_cpu(randrange(0,randrange(50,randrange(100,3000, 50), 50), 50))
            else:
                players[player_counter].add_score(play_hand())
            input("Press enter to resume")
            for player in players.values():
                if player.get_total_score() > highest_score:
                    highest_score = player.get_total_score()
            i += 1
        if highest_score < goal:
            print("\n\nEnd of round\n\n")
            for player in players.values():
                print(f"{player.get_name()} has total of {player.get_total_score()} points")
            input("Press enter to resume")
        
    
    print("\n@@@@@@@@@@@@ Goal has been reached @@@@@@@@@@@@\n")
    
    table = sorted(players.items(), key=lambda item: item[1].get_total_score(), reverse=True)
    for item in table:
        print(f"{item[1].get_name()} scored total of {item[1].get_total_score()} points")
    
        
        
        
