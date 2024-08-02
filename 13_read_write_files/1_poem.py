# todo: poem.txt contains famous poem "Road not taken" by poet Robert Frost.
#  You have to read this file in your python program and find out words with maximum occurrence.
from collections import defaultdict


with open('poem.txt', 'r') as f:
    words = f.read().split()
    # default dict is a dictionary that has a default value for keys that have not been set yet.
    counts = defaultdict(int)

    for word in words:
        word = word.lower().strip(',')
        counts[word] += 1

    max_word = max(counts, key=counts.get)
    print(f'The word with maximum occurrence is "{max_word}" and it occurred {counts[max_word]} times.')
