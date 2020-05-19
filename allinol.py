import collections
from termcolor import colored

from string import ascii_uppercase as alph

def rev():
    #reverses given string
    inp=input("Enter text to be reversed: \n")
    rev = list(reversed(inp))
    print("\n"+''.join(rev), end="\n")
    print("end end end end --------------")

def solve():
    #solves Vigenere's Cipher
    from string import ascii_uppercase as alph
    text = list(input("Enter message: \n").upper())
    key = input("Enter Key: ").upper()
    movedInWord = 0
    
    for i in range(len(text)):
        if text[i] in alph:
            text[i] = chr((ord(text[i])-65-ord(key[movedInWord%len(key)])-65)%26+65)
            movedInWord += 1
    
    print(''.join(text))
    


def findThree():
    #Find patterns of three and three characters and counts them
    text = input("Enter message: \n").upper()
    words = {}
    if text[0] == "@":
        text = list(text)
        for i in range(len(text)-2):
            word = text[i]+text[i+1]+text[i+2]
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
    else:
        ''.join([c for c in text if c in alph or c == ' '])
        text = text.split(" ")
        
        for item in text:
            if len(item) == 3:
                if item in words:
                    words[item] += 1
                else:
                    words[item] = 1
    
    maxKey = ""
    for k,v in words.items():
        try:
            if v > words[maxKey]: maxKey = k
        except:
            maxKey = k
    words={k: v for k, v in sorted(words.items(), key=lambda item: item[1])}
    print(maxKey,words)
 
    
def findVigenereKeyWithLength(n):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    text = "".join(list(filter(lambda c: c in alphabet, input("paste the text: ").upper())))
    
    lists = []
    for i in range(n):
        lists.append([])
        
    for i in range(0, len(text) - n - (len(text) % n), n):
        for j in range(n):
            lists[j].append(text[i+j])
    
    print(text)
    
    keyE = ""
    keyT = ""
    keyA = ""
    
    for t in map("".join, lists):
        print(t)
        mostCommonCharIndex = alphabet.index(collections.Counter(t).most_common(1)[0][0])
        keyE += alphabet[(mostCommonCharIndex - 4) % 26]
        keyT += alphabet[(mostCommonCharIndex - 19) % 26]
        keyA += alphabet[(mostCommonCharIndex - 0) % 26]
        
    print()
    print("In the parts with e as the most common letter:", keyE)
    print("In the parts with t as the most common letter:", keyT)
    print("In the parts with a as the most common letter:", keyA)
    

    
    
#rev()      
#solve()
#findThree()
