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
    text = list(input("Enter message: \n").upper())
    words = {}
    for i in range(len(text)-2):
        word = text[i]+text[i+1]+text[i+2]
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    
    maxKey = ""
    for k,v in words.items():
        try:
            if v > words[maxKey]: maxKey = k
        except:
            maxKey = k
    words={k: v for k, v in sorted(words.items(), key=lambda item: item[1])}
    print(maxKey,words)
 
#rev()      
#solve()
#findThree()