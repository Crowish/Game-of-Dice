#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 11:10:41 2021

@author: crow
"""


def score(dices, show):
    # dices = dictionary of dices
    # assumption: dice out of partial straight gets score
    
    
    score = 0
    straight = True
    partial_low = True
    partial_high = True
    for i in range(1,7):
        if dices.get(i, 0) == 0:
            straight = False
    for i in range(1,6):
        if dices.get(i, 0) == 0:
            partial_low = False
    for i in range(2,7):
        if dices.get(i, 0) == 0:
            partial_high = False
            
    if straight == True:
        if show:
            print("FULL STRAIGHT")
        score = 1500
        return score
    elif partial_low == True:
        if show:
            print("Partial straight 1-5")
        score = 500
        if dices.get(1,0) == 2:
            score += 100
        if dices.get(5,0) == 2:
            score += 50            
        return score
    elif partial_high == True:
        if show:
            print("Partial straight 2-6")
        score = 750
        if dices.get(5,0) == 2:
            score += 50            
        return score        
    else:
        for dice in dices.keys():
            if dices[dice] >= 3:
                if dice == 1:
                    score += 1000 * 2**(dices[dice] - 3)
                else:
                    score += int(dice)* 100 * 2**(dices[dice] - 3)
            elif dice == 1:
                score += dices[dice] * 100
            elif dice == 5:
                score += dices[dice] * 50
        return score