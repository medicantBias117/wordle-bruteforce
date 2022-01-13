## Things got really crazy here. 
## To get more exposure, I went for a random number generator to find possible combinations


from itertools import combinations

# generate random integer values
from random import seed
from random import randint
import random

seed(1)

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

def equalsplit(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

## Prepare the list


wordslist = [];
with open("words_lawl.txt") as file:
	for line in file:
		if(not((line.find("e") > -1) or (line.find("a") > -1)) ):
			wordslist.append(line.rstrip());

#wordslist.sort()
random.shuffle(wordslist)
g = open("console.txt", "w")
g.write(str(wordslist))
g.close()
### create the 4 word combos and create a new list that contains the combinations:
aa = list(equalsplit(wordslist, 5))
wordslist1 = aa[0]
wordslist2 = aa[1]
wordslist3 = aa[2]
wordslist4 = aa[3]
wordslist5 = aa[4]

# for i in range(len(wordslist)*1000*1000*1000*1000):
# 	## find a rand word
# 	word1 = wordslist1[randint(0, len(wordslist1)-1)]
# 	word2 = wordslist2[randint(0, len(wordslist2)-1)]
# 	word3 = wordslist3[randint(0, len(wordslist3)-1)]
# 	word4 = wordslist4[randint(0, len(wordslist4)-1)]
# 	word5 = wordslist5[randint(0, len(wordslist5)-1)]
# 	x = [word1, word2, word3, word4, word5]
	
# 	currentString = "".join(x)
# 	uniqueString = ''.join(set(currentString))
# 	print(x)
# 	if(len(uniqueString) > 22):
# 		f.write(currentString + "," + str(len(uniqueString)) + "\n")
			


for i in range(len(wordslist1)):
	## find a rand word
	word1 = wordslist1[i]
	for j in range(len(wordslist2)):
		word2 = wordslist2[j]
		for k in range(len(wordslist3)):
			word3 = wordslist3[k]
			for l in range(len(wordslist4)):
				word4 = wordslist4[l]
				for m in range(len(wordslist5)):
					word5 = wordslist5[m]
					x = [word1, word2, word3, word4, word5]
					currentString = "".join(x)
					uniqueString = ''.join(set(currentString))
					print(x)
					if(len(uniqueString) > 22):
						f.write(currentString + "," + str(len(uniqueString)) + "\n")
							




