from termcolor import colored
from string import ascii_uppercase as alphabet

#replacements = {"A":None, "B":None, "C":None, "D":None, "E":None, "F":None, "G":None, "H":None, "I":None, "J":None, "K":None, "L":None, "M":None, "N":None, "O":None, "P":None, "Q":None, "R":None, "S":None, "T":None, "U":None, "V":None, "W":None, "X":None, "Y":None, "Z":None}
replacements = {}

text = ""

def printText():
    # Prints the text with the given replacements
    
    for character in text:
        if character in replacements:
            print(replacements[character], end="")
        elif character in alphabet:
            print(colored(character, "yellow"), end="")
        else:
            print(character, end="")

def printReps():
    print(alphabet)
    sorted_replacements = {v: k for k, v in replacements.items()}
    for c in alphabet:
        if c in sorted_replacements:
            print(sorted_replacements[c], end="")
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
        if keys[i] in replacements:
            if replacements[keys[i]] != values[i]:
                print("CONFLICT FOUND with chatacter " + keys[i])
                continue
            
        replacements[keys[i]] = values[i]
        
    printReps()
    printText()
    print()
    