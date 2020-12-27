# import packages
import numpy as np
import random

# Start project by creating word lists

# Shakespear 113 Sonnet
shakespear =  ['Thou', 'art','as','tyrannous','so','as','thou','art',
'as','those','whose','beauties','proudly','make','them','cruel',
'for','well','thou','know','to','my','dear','doting','heart',
'thou','art','the','fairest','and','most','precious','jewel']

# sentence from Courage to Be
tillich = ['what','is','the','courage','to','be','in','a','situation', 
'where', 'the', 'existenialist', 'point', 'of', 'view', 'has',
 'not', 'burst', 'the', 'essentialist', 'framework']

 # space and time
space = ['theory','of','relativity','impossible','to','visulize']

# print out word list 
#for i in space:
    #print(i)

# generate new list with list elements shuffled.
random.shuffle(space)
random.shuffle(tillich)
random.shuffle(shakespear)
print(space)
print(tillich)
print(shakespear)
import random

l = [0, 1, 2, 3, 4]

#print(random.choice(l))