import string
from matplotlib import pyplot as plt
import os

text = input("Message: \n")
text = ''.join(c for c in text if c in string.ascii_letters)

"""
#Single
xy = [[j,0] for j in list(string.ascii_uppercase)]

for i in text:
    xy[ord(i.upper())-65][1] += 1

xy.sort(key=lambda x: x[1], reverse=True)
plt.bar([i[0]for i in xy],[j[1] for j in xy])
"""
"""
#Pair
words = {}
for i in range(0,len(text),2):
    pair = text[i]+text[i+1]
    if pair in words:
        words[pair] += 1
    else:
        words[pair] = 1

words_sorted = {k: v for k, v in sorted(words.items(), key=lambda item: item[1])}
x = [i for i in words_sorted]
y = [j for i,j in words_sorted.items()]
plt.bar(x,y)
"""
plt.show()
os.system('PAUSE')