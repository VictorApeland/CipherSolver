import string
from matplotlib import pyplot as plt
import os

text = input("Message: \n")
text = ''.join(c for c in text if c in string.ascii_letters)

xy = [[j,0] for j in list(string.ascii_uppercase)]

for i in text:
    xy[ord(i.upper())-65][1] += 1

xy.sort(key=lambda x: x[1], reverse=True)

plt.bar([i[0]for i in xy],[j[1] for j in xy])
plt.show()
os.system('PAUSE')