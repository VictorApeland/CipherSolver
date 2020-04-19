from termcolor import colored
from string import ascii_uppercase as alphabet
from matplotlib import pyplot as plt


replacements = {}

text = ""
charLength = 1 # default to cl 1

charSplit = "" if charLength == 1 else " "

encodedCharacters = []



def printText():
    # Prints the text with the given replacements
    
    for encodedCharacter in encodedCharacters:
        if encodedCharacter in replacements:
            print(replacements[encodedCharacter], end=charSplit)
        else:
            if charLength == 1 and encodedCharacter not in alphabet:
                # Proboably punctuation or space
                print(encodedCharacter, end="")
            else:
                print(colored(encodedCharacter, "yellow"), end=charSplit)
       

def printReps():
    oppositeReplacements = {v: k for k, v in replacements.items()}
    if charLength == 1:
        # Print horizontally
        print(alphabet)
        for c in alphabet:
            if c in oppositeReplacements:
                print(oppositeReplacements[c], end="")
            else:
                print("-", end="")
    else:
        # Print vertically
        for c in alphabet:
            print(c, end=": ")
            if c in oppositeReplacements:
                print(oppositeReplacements[c])
            else:
                print("-")
        
    print()
    
def fran():
    # Frequency analyze
    characters = encodedCharacters if charLength != 1 else ''.join(c for c in encodedCharacters if c in alphabet)
    
    frequency = {}
    
    for char in set(characters):
        # make a pair of every unique enccchar and 0
        frequency[char] = 0
    
    for char in characters:
        frequency[char] += 1
        
    # if k not in replacements else replacements[k]
    
    pairs = sorted(frequency.items(), key=lambda item: -item[1])
    
    a,b = map(list,zip(*pairs))
    
    bars = plt.bar(a,b)
    
    for i in range(len(pairs)):
        if pairs[i][0] in replacements:
            bars[i].set_color("r")
            
    plt.show()
    if replacements:
        printReps()



text = input("Paste text: ").upper()


if "$" in text:
    text = text.replace(" ", "") # remove spaces
    # interpret every character before the dollar sign as the number of characters encoding each character
    leng, text = text.split("$")
    charLength = int(leng)

charSplit = "" if charLength == 1 else " "

# Split the text up into charLength-sized chunks
for i in range(0, len(text) - charLength + 1, charLength):
    encodedCharacters.append(text[i:i+charLength])

printText()

run = True

while run:
    
    ass = input("New assumption: ").upper()
    if "=" not in ass:
        # some command is being called
        if ass == "FRAN":
            # Frequency analyze
            fran()
        elif ass == "REVERSE ENCCHARS":
            # Reverse the enchars list, as if the text was reversed before being encoded
            encodedCharacters = list(reversed(encodedCharacters))
            printText()
        elif ass == "REVERSE TEXT":
            # Reverse the entire text, as if the text was reversed after being encoded
            # This is foolish to use after adding to replacements
            text = text[::-1]
            encodedCharacters = []
            
            # Split the text up into charLength-sized chunks
            for i in range(0, len(text) - charLength + 1, charLength):
                encodedCharacters.append(text[i:i+charLength])
            printText()
        elif ass == "RESET":
            replacements = {}
            printText()
        elif ass == "UNDO":
            # undo
            pass
        else:
            # Stop running
            run = False
        continue
    keys, values = ass.split("=")
    if int(len(keys)/charLength) != len(values): 
        if values[-1] == "!":
            # override
            replacements[keys[0]] = values[0]
        else:
            continue
    for i in range(0,len(keys), charLength):
        key = keys[i:i+charLength]
        #if keys[i] in string.ascii_uppercase:
        if key in replacements:
            if replacements[key] != values[int(i/charLength)]:
                print("CONFLICT FOUND with encoded character " + key)
            continue
        
        replacements[key] = values[int(i/charLength)]
        
    printReps()
    printText()
    print()