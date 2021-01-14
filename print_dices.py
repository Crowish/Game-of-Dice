#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 11:52:25 2021

@author: crow
"""

def print_dices(dices):
    #first line
    print("")
    
#    for i in range(1, len(dices)+1):
#        print(f"Dice {i} ", end=" ")
    
    for i in range(1, len(dices)+1):
        print(f"  {i}    ", end=" ")
        
    print("")
    
    
    for dice in dices:
        print(" "+"_" * 5+" ", end=" ")
        
    first_line = {
            1: "     ",
            2: "    *",
            3: "    *",
            4: "*   *",
            5: "*   *",
            6: "*   *"
            }
    
    print("")
    
    for dice in dices:
        print("|"+first_line[dice[0]]+"|", end=" ")
        
    print("")
    
    second_line = {
            1: "  *  ",
            2: "     ",
            3: "  *  ",
            4: "     ",
            5: "  *  ",
            6: "*   *"
            }
    for dice in dices:
        print("|"+second_line[dice[0]]+"|", end=" ")
        
    print("")
    
    third_line = {
            1: "     ",
            2: "*    ",
            3: "*    ",
            4: "*   *",
            5: "*   *",
            6: "*   *"
            }
    for dice in dices:
        print("|"+third_line[dice[0]]+"|", end=" ")
        
    print("")
        
    for dice in dices:
        if dice[1] == True:
            print("stored  ",end="")
        else:
            print(" "*8,end="")
            
    print("\n")