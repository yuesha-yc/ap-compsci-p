huase = ['♦️','♥️','♣️','♠️']
deck = []
for i in huase:
    deck.append(i+'A')
    deck.append(i+'J')
    deck.append(i+'Q')
    deck.append(i+'K')
    for j in range(2,11):
        deck.append(i + str(j))

print(deck)

import random
#洗牌
random.shuffle(deck)
print(deck)
c1 = []
c2 = []
p = []

k = 0
for i in deck:
    if k % 3 == 0:
        c1.append(i)
    elif k % 3 == 1:
        c2.append(i)
    else:
        p.append(i)
    k += 1

print(c1)
print(c2)
print(p)
