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
    
def everyN(n):
    text = input("New assumption: ").upper()
    newText = ""
    for i in range(0,len(text), n):
        newText += text[i]
    return newText



def normal():
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

def pair():
    global text
    text = text[5:]
    if len(text)%2 != 0: return
    while True:
        ass = input("New assumption: ").upper()
        keys, values = ass.split("=")
        if len(keys)/2 != len(values): 
            if values[-1] == "!":
                # override
                replacements[keys[0]] = values[0]
            else:
                continue
        for i in range(0,len(keys),2):
            if keys[i]+keys[i+1] in replacements:
                if replacements[keys[i]+keys[i+1]] != values[i]:
                    print("CONFLICT FOUND with chatacter " + keys[i])
                    continue
            
            replacements[keys[i]+keys[i+1]] = values[i]
        for i in range(0,len(text),2):
            sequence = text[i]+text[i+1]
            if sequence in replacements:
                print(replacements[sequence], end="")
            elif sequence[0] in alphabet and sequence[1] in alphabet:
                print(colored(sequence, "yellow"), end="")
            else:
                print(sequence, end="")
        
    
text = input("Paste text: ").upper()
if text[:5] == "!PAIR":
    print("Entering Pair mode.-.-")
    pair()
else:
    normal()
print()
    