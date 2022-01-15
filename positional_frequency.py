from wordle_words import words
from string import ascii_lowercase
import json

frequencyCounter = {}

for c in ascii_lowercase:
    frequencyCounter[c] = {
        '1' : 0,
        '2' : 0,
        '3' : 0,
        '4' : 0,
        '5' : 0,
    }

def spliter(word):
    return [char for char in word]

for word in words: # Pick up a single word
    letterList = spliter(word)  # Convert it to a list
    print(letterList)

    i = 1    #to keep a track of which number we're playing with
    for letter in letterList: # Update the frequency counter
        frequencyCounter[letter][str(i)] += 1
        i += 1

print (json.dumps(frequencyCounter))