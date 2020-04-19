from collections import deque
from string import ascii_uppercase as alph
setWeights = {"A":0.08167,"B":0.01492,"C":0.02202,"D":0.04253,"E":0.12702,"F":0.02228,"G":0.02015,"H":0.06094,"I":0.06966,"J":0.00153,"K":0.01292,"L":0.04025,"M":0.02406,"N":0.06749,"O":0.07507,"P":0.01929,"Q":0.00095,"R":0.05987,"S":0.06327,"T":0.09356,"U":0.02758,"V":0.00978,"W":0.0256,"X":0.0015,"Y":0.01994,"Z":0.00077,}
#setWeights = {"A":0.1,"B":0.2,"C":0.7}
count = {}
key_length = int(input('Enter key length: '))
text = input("Enter text: ").upper()
text_copy = text
text = [c for c in text if c in alph]


count = {c:0 for c in alph}
output = []
for j in range(key_length):
    
    for i in range(j,len(text),key_length): count[text[i]] += 1
    
    sumOfCount = sum([y for x,y in count.items()])
    givenWeights = {k:v/sumOfCount for k,v in count.items()}
    
    
    maxWeight = [0,0]
    givenFreqList = deque([v for k,v in givenWeights.items()])
    for l in range(len(givenWeights)):
        if l > 0:
            givenFreqList.rotate(-1)
            
        freqSum = sum([givenFreqList[i]*setWeights[chr(i+65)] for i in range(len(givenFreqList))])
        

        if freqSum > maxWeight[1]:
            maxWeight[1] = freqSum
            maxWeight[0] = l
    output.append(maxWeight[0])
    count = {c:0 for c in alph}
  
    
print("")
print(f"Key: {output}")
print("Decrypted version: \n")
#solves the cipher
movedInKey = 0

for i in range(len(text_copy)):
    if text_copy[i] in alph:
        print(chr((ord(text_copy[i])-65-output[movedInKey%len(output)])%26+65),end="")
        movedInKey += 1
    else:
        print(text_copy[i],end="")