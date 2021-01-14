#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 13:25:12 2021

@author: crow
"""
import random
import score
from print_dices import print_dices

NUMBER_OF_DICES = 6
DICE_SIDES = 6

class Hand(object):
#class that handles all dices of a player, contains operations that can be performed on dices
    def __init__(self):
        self.dices = {}
        for i in range(1,NUMBER_OF_DICES+1):
            self.dices["D" + str(i)] = Dice()
    
    def show_hand(self):
        # showing values for all dices
        # TO DO: fancy dices
        if DICE_SIDES == 6:
            dice_lst = []
            for dice in self.dices.values():
                dice_lst.append([dice.get_dice(), dice.is_stored()])
            print_dices(dice_lst)
        else:
            print("\nYour set of dices\n")
            for key in self.dices:
                print(key + ":", self.dices[key].get_dice(), end=", ")
            print("\n")
        
    def store(self,dice_to_store):
        # storing dices, so they won't be rerolled
        # TO DO:    check if at least one dice got stored this turn
        #           check if valid input
        stored_before = 0
        stored_after = 0
        while stored_before == stored_after:
            stored_before = self.count_stored()
            dice_to_store = dice_to_store.split()        
            
            try:
                for dice in dice_to_store:
                    self.dices["D"+dice].store()
            except KeyError:
                print("\nWrong input for storing dices!")
            except:
                print("Man, aren't you crative... unexpected error occured, congratulations!")
                
            stored_after = self.count_stored()
            if stored_before == stored_after:
                dice_to_store = input("You need to store at least one dice that hasn't been stored yet."\
                      "\nTry again: ")
        
    
    def count_stored(self):
        stored = 0
        for dice in self.dices.values():
            if dice.is_stored():
                stored += 1
        return stored
        
    def score(self):
        # returning score counted for dices
        # TO DO: implement function for counting score
        dice_count = {}
        for dice in self.dices.values():
            dice_count[dice.get_dice()] = dice_count.get(dice.get_dice(), 0) + 1
        return score.score(dice_count)
        
    def all_stored(self):
        # returns True if all dices are stored
        flag = True
        for dice in self.dices.values():
            if not dice.is_stored():
                flag = False
        return flag
    
    def reroll_unstored(self):
        # rerolling all unstored dices
        for dice in self.dices.values():
            if not dice.is_stored():
                dice.roll_dice()
    
class Dice(Hand):
    
    def __init__(self):
        self.val = random.randint(1, DICE_SIDES)
        self.stored = False
    
    def get_dice(self):
        #getter for value of dice
        return self.val
    
    def roll_dice(self):
        self.val = random.randint(1, DICE_SIDES)
    
    def store(self):
        # storing dice
        self.stored = True
        
    def is_stored(self):
        #getter returning bool if dice is stored
        return self.stored