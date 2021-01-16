#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 15:40:45 2021

@author: crow
"""

class Player(object):
    cpu_dict = {
            "yes": True,
            "no": False
            }
    i = 1
    def __init__(self, num):
        if num == 1:
            self.cpu = False
        else:
            try:
                self.cpu = Player.cpu_dict[input("\nDo you want Player "+str(num)+" to be cpu? (yes/no)\n")]
            except:
                #print("Error: Wrong input. This player will be set as cpu.")
                print("\nSince user failed to answer simple question, we decided this player will belong to machine")
                self.cpu = True
        if self.cpu == True:
            self.name = "RoboPlayer "+str(Player.i)
            Player.i += 1
        else:
            self.name = input(f"\nSet name for Player {num}\n")
        self.score=0
        
    def get_name(self):
        return self.name
    
    def add_score(self, score):
        self.score += score
        
    def add_score_for_cpu(self, score):
        print("\n.\n.\n.\n.\n"+self.name+" scored "+str(score)+" points")
        self.score += score
        
    def is_cpu(self):
        return self.cpu
    
    def get_total_score(self):
        return self.score
    
    def reset_score(self):
        self.score = 0
    