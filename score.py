#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 11:10:41 2021

@author: crow
"""

def score(dices):
    # dices = dictionary of dices
    # Each 1 	100
    # Each 5 	50
    # Three 1s 	300
    # Three 2s 	200
    # Three 3s 	300
    # Three 4s 	400
    # Three 5s 	500
    # Three 6s 	600
    # more than 3 of a kind = (<score for free>*(<number of dices of a kind>-2)
    # TO DO:
    #       add scoring variations
    score = 0
    straight = 0
    for i in range(1,7):
        straight += dices.get(i, 1)
    if straight == 6:
        print("STRAIGHT (not homophobic tho)")
        score = 3000
        return score
    else:
        for dice in dices.keys():
            if dices[dice] >= 3:
                if dice == 1:
                    score += 300 * (dices[dice] - 2)
                else:
                    score += int(dice)* 100 * (dices[dice] - 2)
            elif dice == 1:
                score += dices[dice]%3 * 100
            elif dice == 5:
                score += dices[dice]%3 * 50
        return score

def score_basic(dices):
    # dices = dictionary of dices
    # Each 1 	100
    # Each 5 	50
    # Three 1s 	300
    # Three 2s 	200
    # Three 3s 	300
    # Three 4s 	400
    # Three 5s 	500
    # Three 6s 	600
    # * all secont three won't be counted
    # TO DO:
    #       add scoring variations
    score = 0    
    for dice in dices.keys():
        if dices[dice] >= 3:
            if dice == 1:
                score += 300
            else:
                score += int(dice)* 100
        elif dice == 1:
            score += dices[dice]%3 * 100
        elif dice == 5:
            score += dices[dice]%3 * 50
    return score