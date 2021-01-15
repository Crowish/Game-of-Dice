#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 13:25:12 2021

@author: crow
"""
import random
import score
from printing import print_dices

NUMBER_OF_DICES = 6
DICE_SIDES = 6

class Hand(object):
#class that handles all dices of a player, contains operations that can be performed on dices
    def __init__(self):
        self.dices = {}
        for i in range(1,NUMBER_OF_DICES+1):
            self.dices["D" + str(i)] = Dice()
        self.hand_score = 0
    
    def show_hand(self):
        # showing all dices
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
        # dices_to_store: string with id's of dice to be stores
        # returns list of store dice
        # storing dices, so they won't be rerolled
        # TO DO:    check if at least one dice got stored this turn
        #           check if valid input
        stored = []
        while len(stored) == 0:
            dice_to_store = dice_to_store.split()        
            try:
                for dice in dice_to_store:
                    ref = self.dices["D"+dice].is_stored()
                    self.dices["D"+dice].store()
                    if ref != self.dices["D"+dice].is_stored():
                        stored.append(dice)                        
            except KeyError:
                print("\nWrong input for storing dices!")
            except:
                print("Man, aren't you crative... unexpected error occured, congratulations!")
            if len(stored) == 0:
                dice_to_store = input("You need to store at least one dice that hasn't been stored yet."\
                      "\nTry again: ")
        return stored
        
    
    def count_stored(self):
        stored = 0
        for dice in self.dices.values():
            if dice.is_stored():
                stored += 1
        return stored
        
    def reroll_valid(self, roll):
        # returning score counted for dices
        # TO DO: implement function for counting score
        dice_count = {}
        for dice in self.dices:
            if dice.strip("D") in roll:
                dice_count[self.dices[dice].get_dice()] = dice_count.get(self.dices[dice].get_dice(), 0) + 1  
        return score.score(dice_count)
    
    def update_score(self, roll):
        dice_count = {}
        for dice in self.dices:
            if dice.strip("D") in roll:
                dice_count[self.dices[dice].get_dice()] = dice_count.get(self.dices[dice].get_dice(), 0) + 1  
        self.hand_score += score.score(dice_count)
        return self.hand_score
        
        
    def all_stored(self):
        # returns True if all dices are stored
        flag = True
        for dice in self.dices.values():
            if not dice.is_stored():
                flag = False
        return flag
    
    def reroll_unstored(self):
        # rerolling all unstored dices
        rerolled = []
        for dice in self.dices:
            if not self.dices[dice].is_stored():
                self.dices[dice].roll_dice()
                rerolled.append(dice.strip("D"))
        return rerolled   
    
    def return_unstored(self):
        # rerolling all unstored dices
        rerolled = []
        for dice in self.dices:
            if not self.dices[dice].is_stored():
                rerolled.append(dice.strip("D"))
        return rerolled
        
    
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
