import numpy as np
import pandas as pd
import string
from apyori import apriori

#Reading in 5 songs from Soft Pop Genre 
with open("song1.txt") as f:
    song_1 = []
    words = f.read().lower().splitlines()
    for i in range(len(words)):
        line_split = words[i].split()
        song_1.append(line_split)
        
with open("song2.txt") as f:
    song_2 = []
    words = f.read().lower().splitlines()
    for i in range(len(words)):
        line_split = words[i].split()
        song_2.append(line_split)

with open("song3.txt") as f:
    song_3 = []
    words = f.read().lower().splitlines()
    for i in range(len(words)):
        line_split = words[i].split()
        song_3.append(line_split)
        
with open("song4.txt") as f:
    song_4 = []
    words = f.read().lower().splitlines()
    for i in range(len(words)):
        line_split = words[i].split()
        song_4.append(line_split)
        
with open("song5.txt") as f:
    song_5 = []
    words = f.read().lower().splitlines()
    for i in range(len(words)):
        line_split = words[i].split()
        song_5.append(line_split)
    
all_songs = []
all_songs.append(song_1)
all_songs.append(song_2)
all_songs.append(song_3)
all_songs.append(song_4)
all_songs.append(song_5)

itemsets = apriori(song_1, min_support=0.3, min_confidence=0.2, min_lift=.1)
# itemsets is a Python generator. We can for-loop through it,
# or force it to fill in by making it a list.
itemsets = list(itemsets)
# Then we can check its length
print('Found', len(itemsets), 'frequent itemsets for song', 1, 'of Soft Pop Music.')
# loop through the list of itemsets
for i, rec in enumerate(itemsets):
    items = list(rec.items) # convert from Python frozenset to list
    print('Itemset {} has support {} with items {}'.format(i, rec.support, items))
# loop through the rules found for this itemset
    for j, rule in enumerate(rec.ordered_statistics):
        print(' {} --> {} confidence: {:.2f} lift: {:.2f}'.format(list(rule.items_base),list(rule.items_add), rule.confidence, rule.lift))
        
 #Running apiori - Genre Soft Pop / Acoustic
for s in range(len(all_songs)):
    count = s + 1
    itemsets = apriori(all_songs[s], min_support=0.3, min_confidence=0.2, min_lift=.1)
    # itemsets is a Python generator. We can for-loop through it,
    # or force it to fill in by making it a list.
    itemsets = list(itemsets)
    # Then we can check its length
    print('SONG', count, ' : ', 'Found', len(itemsets), 'frequent itemsets for song', count, 'of Soft Pop Music.')
    # loop through the list of itemsets
    for i, rec in enumerate(itemsets):
        items = list(rec.items) # convert from Python frozenset to list
        print('Itemset {} has support {} with items {}'.format(i, rec.support, items))
    # loop through the rules found for this itemset
        for j, rule in enumerate(rec.ordered_statistics):
            print(' {} --> {} confidence: {:.2f} lift: {:.2f}'.format(list(rule.items_base),list(rule.items_add), rule.confidence, rule.lift))
    print()
    print()
            
#Reading in 5 songs from Country Genre 
with open("song6.txt") as f:
    song_6 = []
    words = f.read().lower().splitlines()
    for i in range(len(words)):
        line_split = words[i].split()
        song_6.append(line_split)
        
with open("song7.txt") as f:
    song_7 = []
    words = f.read().lower().splitlines()
    for i in range(len(words)):
        line_split = words[i].split()
        song_7.append(line_split)

with open("song8.txt") as f:
    song_8 = []
    words = f.read().lower().splitlines()
    for i in range(len(words)):
        line_split = words[i].split()
        song_8.append(line_split)
        
with open("song9.txt") as f:
    song_9 = []
    words = f.read().lower().splitlines()
    for i in range(len(words)):
        line_split = words[i].split()
        song_9.append(line_split)
        
with open("song10.txt") as f:
    song_10 = []
    words = f.read().lower().splitlines()
    for i in range(len(words)):
        line_split = words[i].split()
        song_10.append(line_split)
        
all_songs1 = []
all_songs1.append(song_6)
all_songs1.append(song_7)
all_songs1.append(song_8)
all_songs1.append(song_9)
all_songs1.append(song_10)

#Running apiori - Country
for s in range(len(all_songs1)):
    count = s + 1
    itemsets = apriori(all_songs1[s], min_support=0.4, min_confidence=0.2, min_lift=.1)
    # itemsets is a Python generator. We can for-loop through it,
    # or force it to fill in by making it a list.
    itemsets = list(itemsets)
    # Then we can check its length
    print('SONG', count, ' : ', 'Found', len(itemsets), 'frequent itemsets for song', count, 'of Country Music.')
    # loop through the list of itemsets
    for i, rec in enumerate(itemsets):
        items = list(rec.items) # convert from Python frozenset to list
        print('Itemset {} has support {} with items {}'.format(i, rec.support, items))
    # loop through the rules found for this itemset
        for j, rule in enumerate(rec.ordered_statistics):
            print(' {} --> {} confidence: {:.2f} lift: {:.2f}'.format(list(rule.items_base),list(rule.items_add), rule.confidence, rule.lift))
    print()
    print()
            

 
