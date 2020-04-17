#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 13:58:41 2020

@author: victorapeland
"""

from termcolor import colored
import string

#problem = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#replacements = {"A":None, "B":None, "C":None, "D":None, "E":None, "F":None, "G":None, "H":None, "I":None, "J":None, "K":None, "L":None, "M":None, "N":None, "O":None, "P":None, "Q":None, "R":None, "S":None, "T":None, "U":None, "V":None, "W":None, "X":None, "Y":None, "Z":None}
replacements = {}
for l in string.ascii_uppercase:
    replacements[l] = "|"

text = ""

def printText():
    # Prints the text with the given replacements
    
    for character in text:
        if character in replacements and replacements[character] != "|":
            print(replacements[character], end="")
        elif character in string.ascii_uppercase:
            print(colored(character, "yellow"), end="")
        else:
            print(character, end="")

def printReps():
    print(string.ascii_uppercase)
    sorted_replacements = {v: k for k, v in replacements.items()}
    for k,repl in sorted_replacements.items():
        if repl != "|":
            print(repl, end="")
        else:
            print("-", end="")

    print()
    
    

text = input("Paste text: ").upper()


while True:
    
    ass = input("New assumption: ").upper()
    keys, values = ass.split("=")
    if len(keys) != len(values): 
        if values[-1] == "!":
            # override
            replacements[keys[0]] = values[0]
        else:
            continue
    for i in range(len(keys)):
        if keys[i] in string.ascii_uppercase:
            if replacements[keys[i]] != values[i] and replacements[keys[i]] != "|":
                print("CONFLICT FOUND with chatacter " + keys[i])
                continue
            
            replacements[keys[i]] = values[i]
        
    printReps()
    printText()
    print()
    
    