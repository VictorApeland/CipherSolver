#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 13:43:56 2020

@author: victorapeland
"""


def isCharacter (c):
    return (("A" <= c) and (c <= "Z")) or (("a" <= c) and (c <= "z"))

text = list(filter(isCharacter, input('Paste text: ')))

keyLength = 0

def printText():
    for i in range(len(text)):
        if (i % keyLength) == 0:
            print()
        print(text[i],end=' ')
        
       

run = True
while run:
    command = input('Write a command: ').lower()
    
    if command[0:2] == 'kl':
        keyLength = int(command[2:])
    elif command == 'print':
        if keyLength > 0:
            printText()
        else:
            print('error, no keyLength set')
    else:
        run = False
    
        