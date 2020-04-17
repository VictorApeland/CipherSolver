# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 18:29:42 2020

@author: hdguy
"""
import string
import os

def equation(a, b, x):
    return int((((x-65)-b)*modInverse(a,26))%26+65);

def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1


anb = input("Value of a,b: ")
anb = [int(x.strip()) for x in anb.split(',')]
a,b = anb[0], anb[1]
text = list(input("Enter text: \n"))

for i in range(len(text)):
    if text[i] in string.ascii_letters:
        text[i] = chr(equation(a,b,ord(text[i])))
print("\n")
print(''.join(text))
os.system('PAUSE')