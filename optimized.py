### First Attempt at Optimization
### Make smaller lists by alphabets
### In a moving window of 5 letters, iterate through each
### Does not do A B C X Y

from itertools import combinations
import cardinality

f = open("ultimate_file.txt", "w")

def next_alpha(s):
    return chr((ord(s.upper())+1 - 65) % 26 + 65).lower()

def evalTheString(comb):
	currentString = "".join((comb))
	uniqueString = ''.join(set(currentString))
	if(len(uniqueString) > 22):
		f.write(currentString + "," + str(len(uniqueString)) + "\n")
		print(currentString)

def doesNotContainDuplicateLetters(word):
	#print (str(word) + str(isinstance(word, list)))
	if(isinstance(word, list)):
		currentString = "".join((word))
		uniqueString = ''.join(set(currentString))
		if(len(uniqueString) < len(currentString)):
			return 0
		else:
			return 1
	else:
		uniqueString = ''.join(set(word))
		if(len(uniqueString) < len(word)):
			return 0
		else:
			return 1

## Prepare the list
wordlist = { "a" : []}
prevLetter = "a"

with open("word_combo_cob.txt") as file:
	for line in file:
		if(prevLetter == line[:1]):
			wordlist[prevLetter].append(line.rstrip())
		else:
			wordlist.update({ line[:1] : [ line.rstrip() ]})
			prevLetter = line[:1]

### create the 5 word combos and create a new list that contains the combinations:

for letter1 in wordlist.keys():	
	for word1 in wordlist[letter1]:
		if(doesNotContainDuplicateLetters(word1)):
			letter2 = next_alpha(letter1)
			for word2 in wordlist[letter2]:
				if(doesNotContainDuplicateLetters([word1,word2])):
					letter3 = next_alpha(letter2)
					for word3 in wordlist[letter3]:
						if(doesNotContainDuplicateLetters([word1,word2,word3])):
							letter4 = next_alpha(letter3)
							for word4 in wordlist[letter4]:
								if(doesNotContainDuplicateLetters([word1,word2,word3,word4])):
									letter5 = next_alpha(letter4)
									for word5 in wordlist[letter5]:
											print([word1,word2,word3,word4,word5])
											evalTheString([word1,word2,word3,word4,word5])
					


