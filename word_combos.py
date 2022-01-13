## Attempt 1 - Basic approach. Find words, use combinations. 
## For each combination, check if the unique count of letters is > 18 (out of a max of 25)
## Best case scenario, we get 24. Leaving only a max of 2 letters to predict.

from itertools import combinations
import cardinality

## Prepare the list
wordslist = [];
with open("final_list.txt") as file:
    for line in file:
    	wordslist.append(line.rstrip());

### create the 5 word combos and create a new list that contains the combinations:
f = open("ultimate_file.txt", "w")

g = combinations(wordslist, 5)

i = 0
for comb in g :
	i = i + 1
	currentString = "".join(comb)
	uniqueString = ''.join(set(currentString))
	if(len(uniqueString) > 18):
		f.write(currentString + "," + str(len(uniqueString)) + "\n")
		print(currentString)
	print(str(i) + " ====== "  )

f.close()